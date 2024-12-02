from django.urls import path
from .views import *
urlpatterns=[
    path('viewuser/',UserView.as_view(),name='viewuser')
]
