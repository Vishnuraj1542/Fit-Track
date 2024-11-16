from django import forms
from .models import *

class Specialist_Form(forms.ModelForm):
    
    class Meta:
        model = Specialist_Details
        fields = '__all__'
