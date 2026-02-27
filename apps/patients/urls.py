from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('appointments/create/', views.appointment_create, name='appointment_create'),
    path('appointments/<int:pk>/', views.appointment_detail, name='appointment_detail'),
    path('appointments/<int:pk>/cancel/', views.appointment_cancel, name='appointment_cancel'),
    path('appointments/<int:pk>/prescription/create/', views.appointment_prescription_create, name='appointment_prescription_create'),
    path('appointments/<int:pk>/invoice/create/', views.appointment_invoice_create, name='appointment_invoice_create'),
    path('doctors/', views.doctors_list, name='doctors_list'),
    path('doctors/<int:pk>/', views.doctor_detail, name='doctor_detail'),
    path('patients/', views.patients_list, name='patients_list'),
    path('patients/<int:pk>/', views.patient_detail, name='patient_detail'),
]
