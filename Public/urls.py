from django.urls import path
from .views import *

urlpatterns=[
    path('userpage/',UserPage.as_view(),name='userpage'),
    path('registration/',UserRegistration.as_view(),name='user_registration'),
    path('submit_complaint/',SubmitComplaintView.as_view(), name='submit_complaint'),
    path('complaintreply/',ReplyView.as_view(),name='complaintreply'),
    path('submitfeedback/', SubmitFeedback.as_view(), name='submitfeedback'),
    path('specialistslist/',SpecialistList.as_view(),name='specialistlist'),
    path('specialist/<int:specialist_id>/chat/', ChatWithSpecialist.as_view(), name='specialistchat'),
    path('viewshop/',ViewShop.as_view(),name='viewshop'),
    path('viewproduct/',ProductView.as_view(),name='productdetails')

]