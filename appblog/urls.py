from xml.dom.minidom import Document
from django.conf import settings
from django.urls import path, include

#from proyecto1.proyecto1.settings import MEDIA_ROOT
from .views import Post_detalle_view, Posteos_lista_view, crear_posteos, editar_usuario, inicio, subir_avatar_view, buscar_posteos, crear_comentarios_view, crear_usuario_view, login_request, register_request, sobre_mi_vista
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', inicio, name="index"), #Default view

    path('login1', login_request, name= "login1"),
    path('logout', LogoutView.as_view(template_name="appblog/logout.html"), name= "logout"),
    path('register', register_request, name= "register"),

    path('editar_perfil', editar_usuario, name ="Editar_perfil"),
    path('subir_avatar', subir_avatar_view , name="subir_avatar"),

    path('post', Posteos_lista_view.as_view(), name= "vista_posteos"),
    path('detalle/post<pk>/', Post_detalle_view.as_view() , name= "detalle_post"),
    path('crear_comentarios_view', crear_comentarios_view, name="Comentarios"),
    path('posteos_buscar', buscar_posteos, name="Buscar_entradas"),
    path('crear_posteos', crear_posteos, name="crear_posteos"),
    path('crear_usuario_view', crear_usuario_view, name="Usuario"),
    path('about_me', sobre_mi_vista, name="Sobre_mi"),
]