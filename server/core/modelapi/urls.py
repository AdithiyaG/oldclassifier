from django.urls import path
from modelapi import views


urlpatterns=[
    path('patientdetails/', views.PatientView.as_view(), name= 'patient_list'),
    path('classifier/', views.ClassifierView.as_view(), name= 'classifier_list'),

]