from django.contrib import admin
from .models import Categorias, Posteos, Comentarios, Avatar_model

admin.site.register(Categorias)
admin.site.register(Posteos)
admin.site.register(Comentarios)
admin.site.register(Avatar_model)