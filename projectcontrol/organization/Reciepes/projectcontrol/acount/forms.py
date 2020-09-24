from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account


class RegistrationForm(UserCreationForm):
    emails = forms.EmailField(max_length=60, help_text='Required. Add a valid email address')

    class Meta:
        model = Account
        fields = (

            "username",
            "password1",
            "password2",
        )
