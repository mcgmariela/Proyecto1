import email
from django import forms

class posteos_forms(forms.Form):

    titulo = forms.CharField(max_length=150)
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