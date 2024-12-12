from django import forms
from .models import *

class Trainer_Form(forms.ModelForm):
    class Meta():
        model=TrainerRegistration
        fields = '__all__'

class TutorialForm(forms.ModelForm):
    class Meta():
        model=Tutorials
        fields = '__all__'