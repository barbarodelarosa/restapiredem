from django.contrib import admin
from blog.models import *

admin.site.register(CategoriaPost)
admin.site.register(Post)
admin.site.register(Comentario)
admin.site.register(Imagen)

# Register your models here.
