from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.about,name='about'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('fix-time/',views.fix_time,name='fix_time'),
    path('patient-confirm/<appointment>',views.patient_confirm,name='patient_confirm'),
    path('send-link/',views.send_link,name='send_link'),
    path('doctor-type',views.doctor_type,name='doctor_type'),
    path('display-doctors/<specialization>',views.display_doctors,name='display_doctors'),
    path('boook-appointment/<doctor_id>',views.book_appointment,name='book_appointment'),
    path('blog/',views.blog,name='blog'),
    path('home/',views.home,name='home'),
    path('patientdashboard/',views.patientdashboard,name='patientdashboard'),
    path('doctordashboard/',views.doctordashboard,name='doctordashboard'),
    path('pendingappointments/',views.pendingappointments,name='pendingappointments'),
    
]
