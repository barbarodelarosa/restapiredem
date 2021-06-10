from django.contrib import admin

from negocio.models import *

admin.site.register(CategoriaNegocio)
admin.site.register(Negocio)

admin.site.register(CategoriaProducto)
admin.site.register(Producto)
admin.site.register(Seguidor)
admin.site.register(Galeria)



# Register your models here.
