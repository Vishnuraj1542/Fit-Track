from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from .models import *
from .forms import *

# Create your views here.
class shop(View):
    def get(self,request):
        return render(request,'Shop/homepage.html')

class ShopRegistration(View):
    def get (self,request):
        return render(request, 'shop/registration.html')
    
    def post(self,request):
        details=ShopForm(request.POST)
        if details.is_valid():
            details.save(commit=False)
            data=LoginDetails.objects.create_user(
                username=request.POST['username'],
                email=request.POST['email'],
                password=request.POST['password'],
                user_type='SHOPKEEPER')
            details.key=data
            details.save()
            return redirect('homepage')
        else:
            return render(request, 'shop/registration.html')


class ProductAdd(View):
    def get(self,request):
        return render(request,'shop/addingpage.html')
    def post(self,request):
        items=ProductForm(request.POST,request.FILES)
        if items.is_valid():
            items.save()
            return HttpResponse('product added')
        return render(request,'addingpage.html')


class ViewPage(View):
    def get(self,request):
        data=Products.objects.all()
        return render(request,'shop/viewpage.html',{'datas':data})

