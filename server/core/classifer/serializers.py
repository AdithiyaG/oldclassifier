from rest_framework import serializers
from .models import ClassifierAPI,PatientAPI


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientAPI
        fields = '__all__'

class ClassifiertSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassifierAPI
        fields = '__all__'