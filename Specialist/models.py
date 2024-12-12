from django.db import models
from Manager.models import LoginDetails

        # Create your models here.
class Specialist_Details(models.Model):
    genders=[('MALE','male'),('FEMALE','female'),('OTHERS','others')]

    name = models.CharField(max_length=44, null=True, blank=True)
    dob = models.IntegerField(null=True, blank=True)
    gender=models.CharField(max_length=44,null=True,blank=True,choices=genders)
    phone=models.IntegerField(null=True,blank=True)
    qualification=models.CharField(max_length=99,blank=True,null=True)
    certificate=models.ImageField(null=True,blank=True,upload_to='pic_specialist')
    experience=models.IntegerField(null=True,blank=True)
    exp_certificate=models.ImageField(null=True,blank=True,upload_to='pic_specialist')
    specialization=models.CharField(max_length=80,blank=True,null=True)
    idproof=models.ImageField(null=True,blank=True,upload_to='pic_specialist')
    photo=models.ImageField(null=True,blank=True,upload_to='pic_specialist')
    key = models.OneToOneField(LoginDetails, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=33, default='active', null=True, blank=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)


class ChatMessage(models.Model):
    sender = models.ForeignKey(LoginDetails, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(LoginDetails, related_name='received_messages', on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender} to {self.receiver} at {self.timestamp}"