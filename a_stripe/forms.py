from django.forms import ModelForm
from django import forms
from .models import *

class ShippingInfoForm(ModelForm):
    class Meta:
        model = ShippingInfo
        exclude = ['user']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Phone'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Last Name'}),
            'address_line_one': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Street Address'}),
            'address_line_two': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Floor/Apartment'}),
            'city': forms.TextInput(attrs={'class': 'form-control','placeholder': 'City'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Zip Code'}),
        }