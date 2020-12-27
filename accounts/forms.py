from django import forms
from django.contrib.auth.models import User

class LoginForm (forms.Form):
    username = forms.CharField(max_length=200,label="kullanıcı adı")
    password = forms.CharField(max_length=200,label="şifre",widget=forms.PasswordInput)
    class meta:
        model=User
        fields=[
           'username',
            'password'
            ]