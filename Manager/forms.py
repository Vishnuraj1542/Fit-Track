from .models import *
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = LoginDetails
        fields = ("username",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = LoginDetails
        exclude = []