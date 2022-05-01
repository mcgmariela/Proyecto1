from dataclasses import fields
import email
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from appblog.models import Usuarios, Avatar_model, Posteos


class posteos_forms(forms.Form):

    titulo = forms.CharField(max_length=150)
    #imagen_post = forms.ImageField()
    contenido = forms.CharField(max_length=2500)
    autor = forms.CharField(max_length=15)
   

class comentarios_forms(forms.Form):

    usuario = forms.CharField(max_length=15)
    comentario = forms.CharField(max_length=250)

class buscar_posteos_forms(forms.Form):

    titulo = forms.CharField(max_length=150)

class usuario_forms(forms.Form):

    nombre = forms.CharField(max_length=15)
    contrasena = forms.CharField(max_length=8)


class usuario_register_forms(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label ='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita la contreña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}


class editar_usuario_forms(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label ='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita la contreña', widget=forms.PasswordInput)

    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        help_text = {k: "" for k in fields}


class avatar_forms(forms.Form):

    imagen = forms.ImageField()


class avatar_subir_forms(forms.Form):

    model = Avatar_model


class sobre_mi_forms(forms.Form):

    resumen = forms.CharField()