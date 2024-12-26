from django.urls import path
from .views import *

app_name = 'Manager'
urlpatterns = [
    path('', login_page.as_view(), name='login'),
    path('homepage/', HomePage.as_view(), name='homepage'),
    path('shop/', ShopPage.as_view(), name='shoppage'),
    path('trainer/',Trainer_Page.as_view(),name='trainerpage'),
    path('specialist/',Specialist_Page.as_view(),name="specialistpage"),
    path('myadmin/',AdminPage.as_view(),name="adminpage"),
]
