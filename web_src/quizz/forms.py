from django import forms
from django.contrib.auth import authenticate, login


class connectForm(forms.Form):
    username = forms.CharField(label="username", required=True, widget=forms.TextInput)
    password = forms.CharField(label="password", required=True, widget=forms.PasswordInput)

