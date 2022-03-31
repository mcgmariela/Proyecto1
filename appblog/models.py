from email.policy import default
from pyexpat import model
from django.db import models
from django.utils import timezone

class Categorias(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return (f"Name: {self.name}")

class Posteos(models.Model):

    #categoria = models.ForeignKey(Categorias, on_delete=models.PROTECT, default=1)
    titulo = models.CharField(max_length=150)
    contenido = models.TextField(max_length=2500)
    autor = models.TextField(max_length=15)
    fecha_publicacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return (f"titulo: {self.titulo}, autor: {self.autor}, fecha_publicacion: {self.fecha_publicacion}")

class Comentarios(models.Model):

    #posteo = models.ForeignKey(Posteos, on_delete= models.CASCADE)
    usuario = models.TextField(max_length=15)
    comentario = models.TextField(max_length=250)

    def __str__(self):
        return (f"usuario: {self.usuario}, comentario: {self.comentario}")


class Usuarios(models.Model):

    nombre = models.CharField(max_length=15)
    contrasena = models.CharField(max_length=8)

    def __str__(self):
        return (f"nombre: {self.nombre}, contrasena: {self.contrasena}")