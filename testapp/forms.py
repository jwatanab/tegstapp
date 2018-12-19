from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm
)
from .models import Account

class AccountForm(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput)

  class Meta:
      model  = Account
      fields = ("username", "password")


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label 
