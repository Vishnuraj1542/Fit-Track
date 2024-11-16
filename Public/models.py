from django.db import models
from Manager.models import LoginDetails


# Create your models here.
class user_details(models.Model):

    name=models.CharField(max_length=55,null=True,blank=True)
    dob=models.DateField(null=True,blank=True)
    gender=models.CharField(max_length=33,blank=True,null=True,choices=[
        ('MALE', 'Male'),
        ('FEMALE', 'Female')])
    phone=models.IntegerField(null=True,blank=True)
    address=models.CharField(max_length=90,null=True,blank=True)
    key=models.OneToOneField(LoginDetails,on_delete=models.CASCADE,blank=True,null=True)
    status=models.CharField(max_length=3,default='active',null=True,blank=True)
    is_active=models.BooleanField(default=True,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)