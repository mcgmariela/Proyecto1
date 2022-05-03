from multiprocessing import AuthenticationError
import django
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

#from proyecto1.appblog.forms import posteos_forms
from .models import Categorias, Comentarios, Posteos, Usuarios, Avatar_model
from .forms import buscar_posteos_forms, posteos_forms, comentarios_forms, usuario_forms, usuario_register_forms, editar_usuario_forms ,avatar_forms, sobre_mi_forms

def inicio(request):
    comienzo_categorias = Categorias.objects.all()
    
    if request.user.username:
        avatar = Avatar_model.objects.filter(usuario=request.user)

        if len(avatar) > 0:
            imagen = avatar[0].imagen.url
        else:
            imagen = None
    else:
        imagen = None

    return render(request, "appblog/test.html" , {"imagen_url" : imagen})

#def vista_posteos(request):
#    posteos = Posteos.objects.all()
#    comienzo_categorias = Categorias.objects.all()
#    return render(request, "appblog/posts.html", {'posteos' : posteos, 'comienzo_categorias' : comienzo_categorias })


def crear_posteos(request):
    posteos = Posteos.objects.all()
    comienzo_categorias = Categorias.objects.all()
    formulario = posteos_forms()

    if request.method == 'POST':
        formulario = posteos_forms(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            print(data)
            entrada = Posteos(titulo = data['titulo'], contenido=data['contenido'])
            entrada.save()
            return render(request, 'appblog/post_formulario.html', {'formulario': formulario, "comienzo_categorias": comienzo_categorias})
    
    else :
        return render(request, 'appblog/post_formulario.html', {'formulario': formulario, "comienzo_categorias": comienzo_categorias})

class Posteos_lista_view(ListView):

    model = Posteos
    template_name = "appblog/post.html"

class Post_detalle_view(DetailView):

    model = Posteos
    template_name = "appblog/detalle_post.html"

#class CursoActualizar(UpdateView):

 #   model = Posteos
  #  success_url = "/appcoder/curso/list"
   # fields = ['nombre']


#class CursoBorrar(DeleteView):

 #   model = Posteos
  #  success_url = "/appcoder/curso/list"



def buscar_posteos(request):
    buscador_posteos = buscar_posteos_forms()
    comienzo_categorias = Categorias.objects.all()
    data = request.GET.get('titulo')
    if data:
        print(data)
        form_with_data = buscar_posteos_forms(request.GET)
        if form_with_data.is_valid():
            titulo_buscado = Posteos.objects.filter(titulo=data).first()
            print (titulo_buscado)
            if (titulo_buscado):
                return render(request, 'appblog/buscar_posteos.html', {"search_form": buscador_posteos,"titulo2": titulo_buscado})
            return render(request, 'appblog/buscar_posteos.html', {"search_form": buscador_posteos,"titulo2": None})

        return render(request, 'appblog/buscar_posteos.html', {"search_form": buscador_posteos, "titulo2": titulo_buscado, "error": form_with_data.errors})
    
    return render(request, 'appblog/buscar_posteos.html', {"search_form": buscador_posteos, "titulo2": None, "error": None, "comienzo_categorias": comienzo_categorias})


def crear_comentarios_view(request):
    comentarios_view = Comentarios.objects.all()
    comienzo_categorias = Categorias.objects.all()
    formulario = comentarios_forms()

    if request.method == 'POST':
        form = comentarios_forms(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            comment = Comentarios(usuario=data['usuario'],comentario=data['comentario'])
            comment.save()
            return render(request, 'appblog/comment_formulario.html', {'formulario': formulario, "comienzo_categorias": comienzo_categorias})
    
    else :
        return render(request, 'appblog/comment_formulario.html', {'formulario': formulario, "comienzo_categorias": comienzo_categorias})


def crear_usuario_view(request):
    usuario_view = Usuarios.objects.all()
    comienzo_categorias = Categorias.objects.all()
    formulario = usuario_forms()

    if request.method == 'POST':
        formulario = usuario_forms(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            print(data)
            user = Usuarios(nombre=data['nombre'],contrasena=data['contrasena'])
            user.save()
            return render(request, 'appblog/usuario_formulario.html', {'formulario': formulario, "comienzo_categorias": comienzo_categorias})
    
    else :
        return render(request, 'appblog/usuario_formulario.html', {'formulario': formulario, "comienzo_categorias": comienzo_categorias})



def login_request(request):

    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            nombre_usuario = data.get("username")
            contrasenia = data.get("password")

            usuario = authenticate(username = nombre_usuario, password = contrasenia)

            if usuario is not None:
                login(request, usuario)
                return redirect("index")
            else:
                return render(request, "appblog/test.html", {"mensaje": "Usuario inexistente"})

        else: 
            return render(request, "appblog/test.html", {"errors": "Usuario inexistente"})

    else:
        formulario = AuthenticationForm()
        return render(request, "appblog/login.html", {'form':formulario})


def register_request(request):

    if request.method == "POST":
        formulario = usuario_register_forms(request.POST)

        if formulario.is_valid():

            usuario = formulario.cleaned_data.get("username")
            print(usuario)
            formulario.save()

            return redirect("index")
        
        else:
            return render(request, "appblog/test.html", {"mensaje": "Usuario ya registrado"})

    else:
        formulario = usuario_register_forms()
        return render(request, "appblog/register.html", {"formulario":formulario})


@login_required()

def editar_usuario(request):

    usuario = request.user

    if request.method == "POST":
        formulario = editar_usuario_forms(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            usuario.email = data["email"]
            usuario.password1 = data["password1"]
            usuario.password2 = data["password2"]
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]

            usuario.save()

            return redirect("index")

        else: 
            formulario = editar_usuario_forms(initial = {"email": usuario.email})
            return render(request, "appbloog/editar_perfil.html", {"form": formulario, "errors":["Datos incorrectos"]})
    
    else:
        formulario = editar_usuario_forms(initial = {"email": usuario.email})
        return render(request, "appblog/editar_perfil.html", {"form": formulario})


@login_required()
def subir_avatar_view(request):

    if request.method == "POST":

        formulario = avatar_forms(request.FILES)

        if formulario.is_valid():

            usuario = request.user

            avatar = Avatar_model.objects.filter(user=usuario)

            if len(avatar) > 0:
                avatar.image = formulario.cleaned_data["imagen"]
                print(avatar)
                avatar.save()

            else:
                avatar = Avatar_model(user = usuario, imagen = formulario.cleaned_data["imagen"])
                print(avatar)
                avatar.save()
        
        return redirect("index")

    else:
        formulario = avatar_forms()
        return render(request, "appblog/subir_avatar.html", {'formulario': formulario})

def sobre_mi_vista(request):

    sobre_mi = sobre_mi_forms()
    return render(request, "appblog/about_me.html")
