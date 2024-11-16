from django import forms
from .models import*

class ShopForm(forms.ModelForm):
    class Meta():
        model=Shop_details
        fields=['owner_name','phone','address','licence_no','gst_no']

class ProductForm(forms.ModelForm):
    class Meta():
        model=Products
        fields= '__all__'