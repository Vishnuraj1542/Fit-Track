from django.urls import path
from .views import *

urlpatterns=[
    path('home/',shop.as_view(),name='homepage'),
    path('registration/',ShopRegistration.as_view(),name='shop_registration'),
    path('addproduct/',ProductAdd.as_view(),name='productadding'),
    path('viewproduct/',ViewPage.as_view(),name='productview'),
    path('deleteproduct/<int:id>/',Delete.as_view(),name='deleteproduct'),
    path('editproduct/<int:id>/',Edit.as_view(),name='editproduct'),
]