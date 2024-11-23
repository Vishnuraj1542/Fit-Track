from django.urls import path
from .views import *

app_name = 'Manager'
urlpatterns = [
    path('', login_page.as_view(), name='login'),
    path('homepage/', HomePage.as_view(), name='homepage'),
    path('shoppage/', ShopPage.as_view(), name='shoppage'),
    path('trainerpage/',Trainer_Page.as_view(),name='trainerpage'),
    path('specialistpage/',Specialist_Page.as_view(),name="specialistpage"),
]
