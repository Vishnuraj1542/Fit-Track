from django.urls import path
from .views import *
from . import views

urlpatterns=[
    path('viewuser/',UserView.as_view(),name='viewuser'),
    path('trainerpost/', TrainingPost.as_view(), name='all_trainer_media'),
    path('trainerpost/<int:trainer_id>/', TrainingPost.as_view(), name='trainer_media'),
    path('specialist/chat/<int:user_id>/', SpecialistChat.as_view(), name='userchat'),
]
