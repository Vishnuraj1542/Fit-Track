from django.urls import path
from . import views
from .views import *

urlpatterns=[
    path('trainerregistration/',TrainerRegistration .as_view(),name='trainer_registration'),
    path('doctorregistration/',Specialist_Registration.as_view(),name='specialist_registration'),
    path('viewtrainers/',TrainerView.as_view(),name='viewtrainers'),
    path('managedoctor/',ManageSpecialist.as_view(),name='managespecialist'),
    path('adminview/',ManageShop.as_view(),name='manage_shop'),
    path('view-all-suggestions/', ViewAllSuggestions.as_view(), name='view_all_suggestions'),
    path('verify/',Verify.as_view(),name='verify'),
    path('verify/<int:id>/',Verify.as_view(),name='changestatus'),
    path('workout/',TrainersPost.as_view(),name='workout'),
    path('trainerstatus/', ManageTrainer.as_view(), name='managetrainer'),
    path('trainerstatus/<int:id>/', ManageTrainer.as_view(), name='managetrainer'),
]