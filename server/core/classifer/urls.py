from django.urls import path
from classifer import views


urlpatterns=[
    path('patientdetails/', views.PatientView.as_view(), name= 'patient_list'),
    path('classifier/', views.ClassifierView.as_view(), name= 'classifier_list'),
    path('report/', views.ReportView.as_view(), name= 'report_list'),

]