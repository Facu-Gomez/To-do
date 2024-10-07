from django import forms
from . import models
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import User, TareaFacultad, TareaTrabajo, Notas


#formularios para usuario: 
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ['username', 'password']

        
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # Excluye 'profile_pic'
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
    

class CustomUserChangeForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username' : forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


#formulario para la facultad:

class TareaFacultadForm(forms.ModelForm):
    fecha_entrega = forms.DateField(
        input_formats=['%Y-%m-%d'], 
        widget=forms.DateInput(attrs={'type': 'date'})  
    )

    class Meta:
        model = TareaFacultad
        fields = ['titulo', 'descripcion', 'fecha_entrega', 'estado']


#formulario para el trabajo:

class TareaTrabajoForm(forms.ModelForm):
    fecha_entrega = forms.DateField(
        input_formats=['%Y-%m-%d'], 
        widget=forms.DateInput(attrs={'type': 'date'}) 
    )

    class Meta:
        model = TareaTrabajo
        fields = ['titulo', 'descripcion', 'fecha_entrega', 'estado']


#formulario para las notas:


class NotasForm(forms.ModelForm):
    class Meta:
        model = Notas
        fields = ['descripcion']