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
    key = models.OneToOneField(LoginDetails, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(default='active', max_length=33, null=True, blank=True)
    is_active = models.BooleanField(default=True, blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)  

