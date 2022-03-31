from django.shortcuts import render

#from proyecto1.appblog.forms import posteos_forms
from .models import Categorias, Comentarios, Posteos, Usuarios
from .forms import buscar_posteos_forms, posteos_forms, comentarios_forms, usuario_forms

def inicio(request):
    comienzo_categorias = Categorias.objects.all()
    return render(request, "appblog/test.html"   )

def vista_posteos(request):
    posteos = Posteos.objects.all()
    comienzo_categorias = Categorias.objects.all()
    return render(request, "appblog/posts.html", {'posteos' : posteos, 'comienzo_categorias' : comienzo_categorias })

def crear_posteos(request):
    posteos = Posteos.objects.all()
    comienzo_categorias = Categorias.objects.all()
    formulario = posteos_forms()

    if request.method == 'POST':
        form = posteos_forms(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            entrada = Posteos(titulo = data['titulo'], contenido=data['contenido'],autor=data['autor'])
            entrada.save()
            return render(request, 'appblog/post_formulario.html', {'formulario': formulario, "comienzo_categorias": comienzo_categorias})
    
    else :
        return render(request, 'appblog/post_formulario.html', {'formulario': formulario, "comienzo_categorias": comienzo_categorias})


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
        form = usuario_forms(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            user = Usuarios(nombre=data['nombre'],contrasena=data['contrasena'])
            user.save()
            return render(request, 'appblog/usuario_formulario.html', {'formulario': formulario, "comienzo_categorias": comienzo_categorias})
    
    else :
        return render(request, 'appblog/usuario_formulario.html', {'formulario': formulario, "comienzo_categorias": comienzo_categorias})
