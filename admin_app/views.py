from django.shortcuts import render,redirect
from django.views import View
from Trainer.forms import *
from django.http import HttpResponse
from Specialist.forms import *


# Create your views here.
class TrainerRegistration(View):
    def get(self,request):
        return render(request,'trainer/registration.html')
    def post(self,request):
        data=Trainer_Form(request.POST,request.FILES)
        if data.is_valid():
            data.save(commit=False)
            details=LoginDetails.objects.create_user(
                username=request.POST['username'],
                email=request.POST['email'],
                password=request.POST['password'],
                user_type='TRAINER'
            )
            data.key=details
            data.save()
            return HttpResponse ('trainer added sucessfully')
        return render(request,'trainer/registration.html')
    

class Specialist_Registration(View):
    def get(self,request):
        return render(request,'specialist/registration.html')
    def post(self,request):
        details= Specialist_Form(request.POST,request.FILES)
        if details.is_valid():
            details.save(commit=False)
            data=LoginDetails.objects.create_user(
                username=request.POST['username'],
                email=request.POST['email'],
                password=request.POST['password'],
                user_type='SPECIALIST'
            )
            details.key=data
            details.save()
            return HttpResponse('specialist added sucessfully')
        return render(request,'specialist/registration.html')