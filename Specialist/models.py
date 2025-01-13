from django.db import models
from Manager.models import LoginDetails
from django.utils.timezone import now


        # Create your models here.
class Specialist_Details(models.Model):
    genders=[('MALE','male'),('FEMALE','female'),('OTHERS','others')]

    name = models.CharField(max_length=44, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    gender=models.CharField(max_length=44,null=True,blank=True,choices=genders)
    phone=models.CharField(max_length=50,null=True,blank=True)
    qualification=models.CharField(max_length=99,blank=True,null=True)
    certificate=models.ImageField(null=True,blank=True,upload_to='pic_specialist')
    experience=models.IntegerField(null=True,blank=True)
    exp_certificate=models.ImageField(null=True,blank=True,upload_to='pic_specialist')
    specialization=models.CharField(max_length=80,blank=True,null=True)
    idproof=models.ImageField(null=True,blank=True,upload_to='pic_specialist')
    photo=models.ImageField(null=True,blank=True,upload_to='pic_specialist')
    key = models.OneToOneField(LoginDetails, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

class Message(models.Model):
    sender = models.ForeignKey(LoginDetails,on_delete=models.CASCADE,related_name='public_sent_messages')
    receiver = models.ForeignKey(LoginDetails,on_delete=models.CASCADE,related_name='public_received_messages')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From {self.sender.username} to {self.receiver.username} at {self.timestamp}"

