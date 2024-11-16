from django import forms
from .models import *


class user_form(forms.ModelForm):
    class Meta():
        model=user_details
        fields=['name','dob','gender','phone','address']
        