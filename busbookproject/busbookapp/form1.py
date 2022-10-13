from busbookapp.models import Driver,Customer,Bus
from django import forms
from django.contrib.auth.forms import UserCreationForm

class DriverForm(forms.ModelForm):
    class Meta:
        model=Driver
        fields='__all__'


class CustomerForm(forms.ModelForm):
    class Meta:
        model= Customer
        fields='__all__'

class BusForm(forms.ModelForm):
    class Meta:
        model = Bus
        fields= '__all__'