from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profesion', 'comentario', 'foto']

class RegistroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellidos")

    class Meta:
        model = User
        fields = ["username", "password", "first_name", "last_name"]

class ProfileExtraForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["profesion", "comentario"]
