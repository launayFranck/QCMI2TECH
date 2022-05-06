from django import forms
from django.contrib.auth import authenticate, login


class connectForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'fadeIn second', 'placeholder': 'Username'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'fadeIn third', 'placeholder': 'Password'}))

