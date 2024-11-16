from django import forms
from .models import *

class Trainer_Form(forms.ModelForm):
    class Meta():
        model=TrainerRegistration
        fields = '__all__'