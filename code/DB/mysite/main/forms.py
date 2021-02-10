from .models import *
from django.forms import ModelForm, TextInput


class UserForm(ModelForm):
    class Meta:
        model = Accounts
        fields = ["login", "pswd"]
        widgets = {
            "login": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Логин'
            }),
            "pswd": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль'
            }),
        }