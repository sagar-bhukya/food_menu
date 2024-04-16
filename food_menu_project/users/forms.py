# this file is used to add fields like email to usercreationform
from django import forms #forms: This is a module in Django that contains classes and functions for managing forms in a web application.
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm): #inherits the usercreationform to add fields
    email=forms.EmailField()

    class Meta:#information about the model 
        model=User
        fields=['username','email','password1','password2']
# after adding fields go to views.py for import RegisterForm