from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UsuarioForm(UserCreationForm):
    nombre_y_apellido = forms.CharField(required=True)
    class Meta:
        model = User
        fields = ['username', 'nombre_y_apellido', 'password1', 'password2']
