from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from .models import LoginDetails
from .form import *


# Create your views here.
class UserRegistration(View):
    def get(self,request):
        return render(request,'user/register.html')
    def post(self,request):
        details=user_form(request.POST) 
        if details.is_valid():
            details.save(commit=False)
            C=LoginDetails.objects.create_user(
                username=request.POST['username'],
                email=request.POST['email'],
                password=request.POST['password'],
                user_type='USER'
            )
            details.USER=C
            print(C)
            details.save()
            return HttpResponse('hii')
        else:
            return render(request,'user/register.html')