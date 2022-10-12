from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
# from account.models import Driver,Customer
# from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2','is_admin','is_customer','is_employee', )

class ContactForm(forms.Form):
    name = forms.CharField(max_length=255)
    age = forms.IntegerField()
    email = forms.EmailField()
    address = forms.CharField(max_length=255)
    contact_no = forms.IntegerField()
    start = forms.CharField(max_length=30)
    end = forms.CharField(max_length=20)
    date = forms.DateField( widget=forms.SelectDateWidget)
    time = forms.TimeField(widget=forms.TimeInput(format='%H:%M:%AM'))
    content = forms.CharField(widget=forms.Textarea)