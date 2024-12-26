from django.db import models
from Manager.models import*

class TrainerRegistration(models.Model):
    name = models.CharField(max_length=44, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to='trainer_images')
    phone = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    experience = models.IntegerField(null=True, blank=True)
    experience_certificate = models.ImageField(blank=True, null=True,upload_to='trainer_images')
    biodata = models.ImageField(blank=True, null=True,upload_to='trainer_images')
    key = models.OneToOneField(LoginDetails, on_delete=models.CASCADE, blank=True, null=True,related_name='trainer')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
class Tutorials(models.Model):
    media=models.FileField(blank=True,null=True,upload_to='tutorial')
    description=models.CharField(max_length=1000,blank=True,null=True,)
    connect=models.ForeignKey(LoginDetails,on_delete=models.CASCADE,blank=True,null=True)
    lock=models.ForeignKey(TrainerRegistration,on_delete=models.CASCADE,blank=True,null=True)
    status=models.CharField(max_length=33,default='active',null=True,blank=True)
    is_active=models.BooleanField(default=True,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated_at=models.DateTimeField(auto_now_add=True,blank=True,null=True)


class Suggestion(models.Model):
    sender=models.ForeignKey(LoginDetails,on_delete=models.CASCADE,blank=True,null=True)
    suggestion=models.TextField(max_length=1000,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    reply = models.TextField(null=True, blank=True)