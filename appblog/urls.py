from django.urls import path
from .views import crear_posteos, inicio, vista_posteos, buscar_posteos, crear_comentarios_view, crear_usuario_view

urlpatterns = [
    path('', inicio, name="index"), #Default view
    path('post', vista_posteos , name= "vista_posteos"),
    path('crear_comentarios_view', crear_comentarios_view, name="Comentarios"),
    path('posteos_buscar', buscar_posteos, name="Buscar_entradas"),
    path('crear_posteos', crear_posteos, name="crear_posteos"),
    path('crear_usuario_view', crear_usuario_view, name="Usuario")
]