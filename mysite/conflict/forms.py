from django import forms
from .models import User_mod
from django.contrib.auth.models import User

class Signup(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password',)


class sign_up_acc(forms.ModelForm):

    class Meta:
        model = User_mod
        fields = ('reason',)

