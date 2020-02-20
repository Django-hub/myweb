from django import forms
from django.core import validators

class LoginForm(forms.Form):
    name=forms.CharField(max_length=40)
    Password=forms.CharField(max_length=40)
    
#This model class will be converted into Database table. Django is responsible for this.

