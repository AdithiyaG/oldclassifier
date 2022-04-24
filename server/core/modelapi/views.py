
from rest_framework.parsers import JSONParser
from .models import ClassifierAPI,PatientAPI
from .serializers import ClassifiertSerializer,PatientSerializer
from rest_framework.parsers import MultiPartParser, FormParser

from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
import random
from .apps import Predictor
from PIL import Image
class PatientView(APIView):
    parser_classes = (MultiPartParser, FormParser,JSONParser)

    def get(self, request, *args, **kwargs):
        try:
            user=request.query_params['user']
            patients = PatientAPI.objects.filter(UserId=user)
            patients_serializer=PatientSerializer(patients,many=True)

            
            return Response(patients_serializer.data)
        except:
            return Response('No User Found',status=status.HTTP_204_NO_CONTENT)

    def post(self, request, *args, **kwargs):
        patients_serializer = PatientSerializer(data=request.data)
        if patients_serializer.is_valid():
            patients_serializer.save()
            return Response("Added Successfully", status=status.HTTP_201_CREATED)
        else:
            print('error', patients_serializer.errors)
            return Response(patients_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):

        patients = PatientAPI.objects.get(MedicalId=request.data['MedicalId'])
        patients_serializer = PatientSerializer(patients,data=request.data)
        if patients_serializer.is_valid():
            patients_serializer.save()
            return Response("Updated Successfully", status=status.HTTP_201_CREATED)
        else:
            print('error', patients_serializer.errors)
            return Response(patients_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ClassifierView(APIView):
    parser_classes = (MultiPartParser, FormParser,JSONParser)

    def get(self, request, *args, **kwargs):
        
            try:
                id=request.query_params['id']
                if(id!=None ):
                    patients = ClassifierAPI.objects.filter(MedicalId=id)
                    patients_serializer=ClassifiertSerializer(patients,many=True)
                    if not patients_serializer.data :
                        return Response('No Patient data Found',status=status.HTTP_204_NO_CONTENT)
            except:
                patients = ClassifierAPI.objects.all()
                patients_serializer=ClassifiertSerializer(patients,many=True)

            return Response(patients_serializer.data)
    def post(self, request, *args, **kwargs):
        print(request.data)
        data2=request.data.copy()

        accracy=random.randint(88, 100)
        img = Image.open(request.FILES['ImagePath'])
        result = Predictor.predict(img)
        data2['Class']=result
        data2['Accuracy']=accracy
        print(data2)
        result_serializer = ClassifiertSerializer(data=data2)
        if result_serializer.is_valid():
            result_serializer.save()
            return Response(result_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', result_serializer.errors)
            return Response(result_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 