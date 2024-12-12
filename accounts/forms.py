from django import forms
from django.contrib.auth.models import User
from .models import DataEntry

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class DataEntryForm(forms.ModelForm):
    class Meta:
        model = DataEntry
        fields = ['title', 'description']