from django.shortcuts import render
from account.models import Doctor,Patient
from .models import *
from django.contrib.auth.decorators import login_required


# Create your views here.

def about(request):
    if request.user.is_authenticated:
        return render(request,'home4.html')
    else:
        return render(request,'about.html')

def contact(request):
        return render(request,'contact.html')


@login_required(login_url='/')
def home(request):
    return render(request,'home4.html')


@login_required(login_url='/')
def patientdashboard(request):
    pf = Patient.objects.get(email=request.user)
    com_appointments = Appointment.objects.filter(patient=pf,is_completed=True)
    pend_appointments = Appointment.objects.filter(patient=pf,is_completed=False)
    return render(request,'patientdashboard.html',{'pf':pf,'pend_appointments':pend_appointments,'com_appointments':com_appointments})
   

@login_required(login_url='/')
def doctordashboard(request):
    pf = Doctor.objects.get(email=request.user)
    appointments = Appointment.objects.filter(doctor=pf,is_completed=True)
    return render(request,'doctordashboard.html',{'pf':pf,'appointments':appointments})


@login_required(login_url='/')
def pendingappointments(request):
    pf = Doctor.objects.get(email=request.user)
    appointments = Appointment.objects.filter(doctor=pf,is_completed=False)
    return render(request,'pendingappointments.html',{'pf':pf,'appointments':appointments})


@login_required(login_url='/')
def display_doctors(request,specialization):
    specialization = specialization.lower()
    doctors = Doctor.objects.filter(specialization=specialization,is_verified=True)
    return render(request,'doctors.html',{'doctors':doctors})


@login_required(login_url='/')
def book_appointment(request,doctor_id):
    print(request.user)
    doctor = Doctor.objects.get(id=doctor_id)
    patient = Patient.objects.get(email=request.user)
    Appointment.objects.create(patient=patient,doctor=doctor)

    return render(request,'doctors.html')


@login_required(login_url='/')
def doctor_type(request):
    specializations = Specialization.objects.all()
    return render(request,'selecttypeofdoctor.html',{'specializations':specializations})


@login_required(login_url='/')
def blog(request):
    Posts=Post.objects.all()
    return render(request,"blog.html",{'allPosts':Posts})


@login_required(login_url='/')
def fix_time(request):
    appointment = request.POST.get('appointment_id')
    time = request.POST.get('date')
    appointment = Appointment.objects.get(id=appointment)
    appointment.time = time
    appointment.save()
    pf = Doctor.objects.get(email=request.user)
    appointments = Appointment.objects.filter(doctor=pf,is_completed=True)
    return render(request,'doctordashboard.html',{'pf':pf,'appointments':appointments})


@login_required(login_url='/')
def patient_confirm(request,appointment):
    appointment = Appointment.objects.get(id=appointment)
    appointment.is_confirmed = True
    appointment.save()
    pf = Patient.objects.get(email=request.user)
    com_appointments = Appointment.objects.filter(patient=pf,is_completed=True)
    pend_appointments = Appointment.objects.filter(patient=pf,is_completed=False)
    return render(request,'patientdashboard.html',{'pf':pf,'pend_appointments':pend_appointments,'com_appointments':com_appointments})


@login_required(login_url='/')
def send_link(request):
    appointment = request.POST.get('appointment_id')
    link = request.POST.get('link')
    appointment = Appointment.objects.get(id=appointment)
    appointment.link = link
    appointment.save()
    pf = Doctor.objects.get(email=request.user)
    appointments = Appointment.objects.filter(doctor=pf,is_completed=False)
    return render(request,'pendingappointments.html',{'pf':pf,'appointments':appointments})
