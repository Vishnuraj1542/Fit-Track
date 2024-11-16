from django.urls import path 
from .views import *

urlpatterns=[
    path('trainerregistration/',TrainerRegistration .as_view(),name='trainer_registration'),
    path('doctorregistration/',Specialist_Registration.as_view(),name='specialist_registration')
]