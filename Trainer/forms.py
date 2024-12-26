from django import forms
from .models import *

class Trainer_Form(forms.ModelForm):
    class Meta():
        model=TrainerRegistration
        exclude = ['key']
        fields = '__all__'

class TutorialForm(forms.ModelForm):
    class Meta():
        model=Tutorials
        fields = '__all__'

class SuggestionForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        fields = ['suggestion']

class SuggestionReplyForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        fields = ['reply']



