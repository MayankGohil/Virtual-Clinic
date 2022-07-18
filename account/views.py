from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.views import View
from .models import *

# Create your views here.

class Register(View):
   
    def get(self,request,role=None):
        if role == 'Doctor':
            return render(request,'registerdoctor.html')
        elif role == 'Patient':
            return render(request,'register.html')


    def post(self,request,role=None):
             
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        username = request.POST.get('username')
        phone = request.POST.get('phone') 
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')


        if password1 == password2 :
            if User.objects.filter(username__exact=username).exists() : 
                err = 'Username already taken'
                    
            elif User.objects.filter(email__exact=email).exists() :
                err = 'Email already taken'
                    
            else:
                if role == 'Doctor':
                    photo = request.POST.get('photo')
                    degree = request.POST.get('degree')
                    specialization = request.POST.get('specializations')
                    experience = request.POST.get('experience')
                    user = Doctor.objects.create_user(first_name=first_name,last_name=last_name,username=username,phone=phone,
                    email=email,password=password1,experience=experience,photo=photo,specialization=specialization,degree=degree,is_doctor=True)
                elif role == 'Patient':
                    user = Patient.objects.create_user(first_name=first_name,last_name=last_name,username=username,
                    email=email,password=password1,is_patient=True)
    
                user.save()
                
                context = {
                    'username'  : username,
                    'message'   : "User Successfully created",
                    'message_class' : 'success'

                }
                return render(request,'register.html',context)
                
        else:
            err = 'Passwords does not match'
        
        context = {
            'message' : err ,
            'message_class' : 'danger',
            'form' : form
        }
        
        return render(request,'register.html',context)
        

class Login(View):

    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return render(request,'home4.html')
        else:
            return render(request,'register.html')

    
    def post(self,request,*args,**kwargs):
        email = request.POST['email']
        password = request.POST['password']
        
        user = auth.authenticate(email=email,password=password)
                
        if user is not None:
            auth.login(request,user)
            if 'next' in request.POST:
                try:
                    return redirect(request.POST.get('next'))
                except:
                    return render(request,'home4.html')
            else:
                return render(request,'home4.html')

        else:
            context = {
                'message' : 'Invalid Email or Password',
                'message_class' : 'danger'
            }
            return render(request,'register.html',context)

        
class Logout(View):
    def get(self,request,*args,**kwargs):
        auth.logout(request)
        return render(request,'about.html')

class Ask(View):
    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return render(request,'home4.html')
        else:
            return render(request,'ask.html')
  
