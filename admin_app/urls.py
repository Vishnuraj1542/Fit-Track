from django.urls import path
from . import views
from .views import *

urlpatterns=[
    path('trainerregistration/',TrainersRegistration .as_view(),name='trainer_registration'),
    path('doctorregistration/',Specialist_Registration.as_view(),name='specialist_registration'),
    path('adminview/',ManageShop.as_view(),name='manage_shop'),
    path('view-all-suggestions/', ViewAllSuggestions.as_view(), name='view_all_suggestions'),
    path('verify/',Verify.as_view(),name='verify'),
    path('verify/<int:id>/',Verify.as_view(),name='changestatus'),
    path('workout/',TrainersPost.as_view(),name='workout'),
    path('trainerstatus/', ManageTrainer.as_view(), name='managetrainer'),
    path('trainerstatus/<int:id>/', ManageTrainer.as_view(), name='managetrainer'),
    path('viewtrainers/',TrainerView.as_view(),name='viewtrainers'),
    path('edittrainer/<int:id>/',EditTrainer.as_view(),name='edittrainer'),
    path('managedoctor/',SpecialistView.as_view(),name='managespecialist'),
    path('editdoctor/<int:id>',EditSpecialist.as_view(),name='editspecialist'),
    path('deletedoctor/<int:id>/',DeleteSpecialist.as_view(),name='deletespecialist'),
    path('view_complaints/',ViewComplaintsView.as_view(), name='view_complaints'),
    path('reply_complaint/<int:pk>/',ReplyComplaintView.as_view(), name='reply_complaint'),
    path('userrating/',UserRating.as_view(),name='ratingandfeedback')
]