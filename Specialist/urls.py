from django.urls import path
from .views import *
urlpatterns=[
    path('viewuser/',UserView.as_view(),name='viewuser'),

    path('trainerpost/', TrainingPost.as_view(), name='all_trainer_media'),  # No trainer_id
    path('trainerpost/<int:trainer_id>/', TrainingPost.as_view(), name='trainer_media'),]
