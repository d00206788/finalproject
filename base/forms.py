from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.forms import EmailField

# Reordering Form and View


class PositionForm(forms.Form):
    position = forms.CharField()

