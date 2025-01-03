from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.views import View
from .models import *
from .forms import *
from Public .models  import*


# Create your views here.
class shop(View):
    def get(self,request):
        return render(request,'Shop/homepage.html')
    
    #shop owner regisration
class ShopRegistration(View):
    def get (self,request):
        return render(request, 'shop/trainer_register.html')
    
    def post(self,request):
        details=ShopForm(request.POST)
        if details.is_valid():
            details.save(commit=False)
            data=LoginDetails.objects.create_user(
                username=request.POST['username'],
                email=request.POST['email'],
                password=request.POST['password'],
                user_type='SHOPKEEPER',
            )
            details.key=data
            details.save()
            return redirect('homepage')
        else:
            return render(request, 'shop/trainer_register.html')

  # adding products

class ProductAdd(View):
    def get(self,request):
        return render(request,'shop/addingpage.html')
    def post(self,request):
        items=ProductForm(request.POST,request.FILES)
        if items.is_valid():
            items.save()
            return redirect('homepage')
        return render(request,'addingpage.html')

#view page 

class ViewPage(View):
    def get(self,request):
        data=Products.objects.all()
        return render(request,'shop/viewpage.html',{'datas':data})
    
# delete products

class Delete(View):
    def get(self,request,id):
        data=get_object_or_404(Products,pk=id)
        return render(request,'shop/confirmation.html',{'datas':data})
    def post(self,request,id):
        data=get_object_or_404(Products,pk=id)
        data.delete()
        return redirect('productview')
    
#edit product

class Edit(View):
    def get(self,request,id):
        form=Products.objects.get(pk=id)
        return render(request,'shop/edit_page.html',{'data':form})
    def post(self,request,id):
        data=Products.objects.get(pk=id)
        form=ProductForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return redirect('productview')
        return render(request,'shop/edit_page.html',{'form':form})

class UserView(View):
    def get(self,request):
        user_data=user_details.objects.all()
        return render(request,'shop/user_details.html',{'user_data':user_data})