from django.apps import AppConfig
from transformers import ViTFeatureExtractor, ViTForImageClassification
from PIL import Image
import cv2
import numpy as np
from skimage import img_as_float64
from typing import Optional
import types

class ClassiferConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'classifer'

class Predictor(AppConfig):
    SIGMA_LIST = [15, 80, 250]
    ALPHA = 125.0
    BETA = 46.0
    G = 5.0
    OFFSET = 25.0
    name = 'Predict'
    model_path = "F:/Study Material/Capstone/vit-breakhis-all-20220502T204711Z-001/vit-breakhis-all/checkpoint-2000"
    feature_extractor = ViTFeatureExtractor.from_pretrained(model_path)
    model = ViTForImageClassification.from_pretrained(model_path)
    @classmethod
    def singleScale(cls,img,sigma):
        """
        Single-scale Retinex
        
        Parameters :

        img : input image
        sigma : the standard deviation in the X and Y directions, for Gaussian filter
        """

        ssr = np.log10(img) - np.log10(cv2.GaussianBlur(img,(0,0),sigma))
        return ssr
    @classmethod
    def multiScale(cls,img,sigmas : list):
        """
        Multi-scale Retinex
        
        Parameters :

        img : input image
        sigma : list of all standard deviations in the X and Y directions, for Gaussian filter
        """
        retinex = np.zeros_like(img)
        for s in sigmas:
            retinex += cls.singleScale(img, s)

        msr = retinex/len(sigmas)
        return msr
    @classmethod
    def crf(cls,img, alpha, beta):
        """
        CRF (Color restoration function)

        Parameters :

        img : input image
        alpha : controls the strength of the nonlinearity
        beta : gain constant
        """
        img_sum = np.sum(img,axis=2,keepdims=True)

        color_rest = beta * (np.log10(alpha*img) - np.log10(img_sum))
        return color_rest

    @classmethod
    def MSRCR(cls,img, sigmas :list, alpha, beta, G, b):
        """
        MSRCR (Multi-scale retinex with color restoration)

        Parameters :

        img : input image
        sigmas : list of all standard deviations in the X and Y directions, for Gaussian filter
        alpha : controls the strength of the nonlinearity
        beta : gain constant
        G : final gain
        b : offset
        """
        img = img_as_float64(img)+1

        img_msr = cls.multiScale(img, sigmas)    
        img_color = cls.crf(img, alpha, beta)    
        img_msrcr = G * (img_msr*img_color + b)
        
        
        for i in range(img_msrcr.shape[2]):
            img_msrcr[:, :, i] = (img_msrcr[:, :, i] - np.min(img_msrcr[:, :, i])) / \
                                    (np.max(img_msrcr[:, :, i]) - np.min(img_msrcr[:, :, i])) * \
                                    255

        img_msrcr = np.uint8(np.minimum(np.maximum(img_msrcr, 0), 255))
        
        return img_msrcr
    @classmethod
    def clahe_image(cls,colorimage):
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        colorimage_b = clahe.apply(colorimage[:,:,0])
        colorimage_g = clahe.apply(colorimage[:,:,1])
        colorimage_r = clahe.apply(colorimage[:,:,2])
        colorimage_clahe = np.stack((colorimage_b,colorimage_g,colorimage_r), axis=2)
        return colorimage_clahe
    @classmethod
    def preprocess(self,img):
        img = np.array(img)
        img = img[:,:,::-1].copy()
        img = self.clahe_image(img)
        img = self.MSRCR(img,self.SIGMA_LIST,self.ALPHA,self.BETA,self.G,self.OFFSET)
        img = cv2.medianBlur(img,3)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        return img
    @classmethod
    def predict(cls,img):
        img = cls.preprocess(img)
        inputs = cls.feature_extractor(images=img, return_tensors="pt")
        outputs = cls.model(**inputs)
        logits = outputs.logits

        predicted_class_idx = logits.argmax(-1).item()
        return cls.model.config.id2label[predicted_class_idx]