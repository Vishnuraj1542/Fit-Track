from django import forms
from .models import *

class user_form(forms.ModelForm):
    class Meta():
        model=user_details
        fields=['name','dob','gender','phone','address']

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['complaint_text']
        widgets = {
            'complaint_text': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }

        