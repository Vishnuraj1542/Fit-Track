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
    USER=models.ForeignKey(LoginDetails,on_delete=models.CASCADE,blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)

class Complaint(models.Model):
    sender = models.ForeignKey(LoginDetails, on_delete=models.CASCADE, blank=True, null=True)
    complaint_text = models.TextField(max_length=1000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    reply = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('resolved', 'Resolved'),
        ('under_review', 'Under Review'),
        ('closed', 'Closed'),
    ], default='pending')

def __str__(self):
    return f"{self.sender.username}"


class Feedback(models.Model):
    user = models.ForeignKey(LoginDetails, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=0)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.user.username}"


