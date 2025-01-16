from django.db import models
from Manager.models import LoginDetails
 # Create your models here.
class Shop_details(models.Model):
    owner_name = models.CharField(max_length=33, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=55, null=True, blank=True)
    licence_no = models.CharField(max_length=44, null=True, blank=True)
    gst_no = models.CharField(max_length=30, null=True, blank=True)
    key = models.OneToOneField(LoginDetails, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(default='active', max_length=44, null=True, blank=True)
    is_active = models.BooleanField(default=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)



class Products(models.Model):
    product_name=models.CharField(max_length=88,null=True,blank=True)
    description=models.CharField(max_length=300,null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    brand=models.CharField(max_length=100,null=True,blank=True)
    product_image=models.ImageField(null=True,blank=True,upload_to='product_images')
    seller_name=models.CharField(max_length=90,null=True,blank=True)
    status=models.CharField(default='active',max_length=20,null=True,blank=True)
    is_active=models.BooleanField(default=True,null=True,blank=True)
    updated_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)


