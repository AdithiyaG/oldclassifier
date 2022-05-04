from email.headerregistry import ContentDispositionHeader
from rest_framework.parsers import JSONParser
from .models import ClassifierAPI,PatientAPI
from .serializers import ClassifiertSerializer,PatientSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from django.http import FileResponse,HttpResponse
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from datetime import date
from .apps import Predictor
import PIL
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph

class PatientView(APIView):
    parser_classes = (MultiPartParser, FormParser,JSONParser)

    def get(self, request, *args, **kwargs):
        try:
            user=request.query_params['user']
            patients = PatientAPI.objects.filter(UserId=user)
            patients_serializer=PatientSerializer(patients,many=True)
            return Response(patients_serializer.data)
        except:
            try:
                count=request.query_params['count']
                patients=PatientAPI.objects.all().count()
                return Response(patients)
            except:
                return Response('No User Found',status=status.HTTP_204_NO_CONTENT)

    def post(self, request, *args, **kwargs):
        patients_serializer = PatientSerializer(data=request.data)
        if patients_serializer.is_valid():
            patients_serializer.save()
            return Response("Added Successfully", status=status.HTTP_201_CREATED)
        else:
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
        img = PIL.Image.open(request.FILES['ImagePath'])
        result = Predictor.predict(img)
        data2['Class']=result
        result_serializer = ClassifiertSerializer(data=data2)
        if result_serializer.is_valid():
            result_serializer.save()
            return Response(result_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', result_serializer.errors)
            return Response(result_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, *args, **kwargs):
        id=request.query_params['pid']
        patients = ClassifierAPI.objects.get(Id=id)
        patients_serializer = ClassifiertSerializer(patients,data=request.data)
        if patients_serializer.is_valid():
            patients_serializer.save()
            return Response("Updated Successfully", status=status.HTTP_201_CREATED)
        else:
            print('error', patients_serializer.errors)
            return Response(patients_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

class ReportView(APIView):
    parser_classes = (MultiPartParser, FormParser,JSONParser)
    
    def get(self,request):
        id=request.query_params['pid']
        if(id!=None ):
            result = ClassifierAPI.objects.filter(Id=id)
            MedicalId=result[0].MedicalId
            useddate=result[0].UsedDate
            patient = PatientAPI.objects.filter(MedicalId=MedicalId)
            today = date.today()
            d2 = useddate.strftime("%B %d, %Y")
            l=['Name','Gender','Age']
            l1=[]
            r=['Date of Birth','Height','Weight']
            r1=[]
            print(str(result[0].ImagePath))
            for x in patient:
                l1.append(x.PatientName)
                l1.append(x.PatientGender)
                l1.append(str(x.PatientAge))
            for x in patient:
                r1.append(str(x.PatientDOB))
                r1.append(str(x.PatientHeight))
                r1.append(str(x.PatientWeight))
            buf=io.BytesIO()
            c=canvas.Canvas(buf,pagesize=letter)
            c.drawInlineImage('3rd.png',30,600,200,200)
            tdate = c.beginText(400,700)
            tdate.textLine(d2)
            c.drawText(tdate)
            c.line(40,660,550,660)
            thead=c.beginText(40,620)
            thead.textLine('Oncogenomics Report for ID '+ str(MedicalId))
            c.setFontSize(18)
            c.drawText(thead)
            c.line(40,600,550,600)
            c.setStrokeColorRGB(0.75,0.75,0.75)
            c.rect(40,580,520,-100)
            left=c.beginText(60,560)
            for x in l:
                left.textLine(x)
                left.textLine('')
            c.setFontSize(13)
            c.drawText(left)
            leftv=c.beginText(105,560)
            for x in l1:
                leftv.textLine(':  '+x)
                leftv.textLine('')
            c.setFontSize(13)
            c.drawText(leftv)
            right=c.beginText(340,560)
            for x in r:
                right.textLine(x)
                right.textLine('')
            c.setFontSize(13)
            c.drawText(right)
            rightv=c.beginText(430,560)
            for x in r1:
                rightv.textLine(':  '+x)
                rightv.textLine('')
            c.setFontSize(13)
            c.drawText(rightv)
            c.drawString(40,450,'Result :')
            rv=c.beginText(90,450)
            rv.textLine(result[0].Class)
            c.drawText(rv)
            c.drawString(40,420,'Specimen Image used :')
            breast=PIL.Image.open(result[0].ImagePath)
            c.drawInlineImage(breast,40,200,150,150)
            c.drawString(40,150,'Specimen :')
            typeview=c.beginText(130,150)
            typeview.textLine(result[0].type)
            c.drawText(typeview)
            c.drawString(40,100,'Remarks :')
            remarksview=c.beginText(130,100)
            remarksview.textLine(result[0].remarks)
            c.drawText(remarksview)
            c.showPage()
            c.save()
            buf.seek(0)
            filename=l1[0]+'_'+str(useddate)
            
            response =HttpResponse(buf,content_type='application/pdf')
            response.headers['Content-Disposition'] = '"{}"'.format(filename)
            print(response)
            return response

