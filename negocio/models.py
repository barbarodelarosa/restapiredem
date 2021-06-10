import datetime
from django.utils import timezone
from django.db import models
from usuario.models import User, OwnerModel
import uuid
import os

def nombreArchivo(instance, filename):

    nombre = filename.split('.')
    extension = nombre[-1]
    print(uuid.uuid4())
    idfoto = str(uuid.uuid4())
    nombrefinal = os.path.join(idfoto + '.' + extension)
    print(nombrefinal)
    return '/'.join(['imagenes/negocio', str(instance.nameclass), nombrefinal])



class CategoriaNegocio(models.Model):
    nameclass = 'CategoriaNegocio'
    nombre=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to=nombreArchivo, blank=True, null=True)
    creado = models.DateTimeField(default=timezone.now)
    actualizado = models.DateTimeField(blank=True, null=True, auto_now=True)


    def __str__(self):
        return self.nombre


class Negocio(OwnerModel):
    nameclass = 'Negocio'
    categoria=models.ForeignKey(CategoriaNegocio, on_delete=models.CASCADE, related_name='categoria_negocio')
    nombre=models.CharField(max_length=140)
    descripcion=models.CharField(max_length=300, blank=True, null=True)
    logo=models.ImageField(upload_to=nombreArchivo, blank=True, null=True)
    postada=models.ImageField(upload_to=nombreArchivo, blank=True, null=True)
    creado=models.DateTimeField(default=timezone.now)
    actualizado=models.DateTimeField(blank=True, null=True, auto_now = True)
    votos=models.IntegerField(default=0, blank=True)
    mision = models.CharField(max_length=300, blank=True, null=True)
    vision = models.CharField(max_length=300, blank=True, null=True)
    seguidores=models.ManyToManyField(User, related_name='seguidores_negocio', blank=True)
    compartido = models.IntegerField(default=0)
    aprobado = models.BooleanField(default=False)
    telefono = models.CharField(max_length=15, blank=True, null=True, unique=True)
    movil = models.CharField(max_length=15, blank=True, null=True, unique=True)
    correo = models.EmailField(blank=True, null=True, max_length=30, unique=True)
    sitio_web = models.URLField(blank=True, null=True, max_length=30, unique=True)
    facebook = models.URLField(blank=True, null=True, max_length=30, unique=True)
    instagram = models.URLField(blank=True, null=True, max_length=30, unique=True)
    whatsapp = models.URLField(blank=True, null=True, max_length=30, unique=True)
    telegram = models.URLField(blank=True, null=True, max_length=30, unique=True)
    pais = models.CharField(default='Cuba', max_length=25)
    provincia = models.CharField(blank=True, null=True, max_length=25)
    municipio = models.CharField(blank=True, null=True, max_length=25)
    localidad = models.CharField(blank=True, null=True, max_length=25)
    calle = models.CharField(blank=True, null=True, max_length=25)
    coordenadas = models.CharField(max_length=60, blank=True, null=True)
    productos = models.ManyToManyField('Producto', blank=True, related_name='productos')


    def aprovado(self):
        self.aprobado = True
        self.save()


    def __str__(self):
        return "%s %s" %(self.categoria, self.nombre)




class CategoriaProducto(models.Model):
    nameclass = 'CategoriaProducto'
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to=nombreArchivo, blank=True, null=True)
    creado = models.DateTimeField(default=timezone.now)
    actualizado = models.DateTimeField(blank=True, null=True, auto_now=True)

    def __str__(self):
        return self.nombre


class Producto(OwnerModel):
    nameclass = 'Producto'
    # negocio = models.ForeignKey(Negocio, on_delete=models.CASCADE,  related_name='negocio_producto')
    categoria=models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE, related_name='categoria_producto')
    nombre=models.CharField(max_length=140)
    descripcion=models.CharField(max_length=1500, blank=True, null=True)
    imagen=models.ImageField(upload_to=nombreArchivo, blank=True, null=True)
    creado=models.DateTimeField(default=timezone.now)
    actualizado=models.DateTimeField('Fecha de actualizacion', blank=True, null=True, auto_now = True)
    votos=models.IntegerField(default=0, blank=True)
    aprobado = models.BooleanField(default=False)
    precio = models.FloatField(default=0.00)

    def aprovado(self):
        self.aprobado = True
        self.save()

    def __str__(self):
        return  "%s %s" %(self.categoria, self.nombre)

    def fecha_publicado(self):
        return self.creado >= timezone.now() - datetime.timedelta(days=1)




class Seguidor(models.Model):
    negocio = models.ForeignKey(Negocio, on_delete=models.CASCADE, related_name='negocio_seguidor')
    usuario = models.ManyToManyField(User, related_name='perfil_seguidor')
    creado = models.DateTimeField(default=timezone.now)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.negocio, self.usuario






class Galeria(OwnerModel):
    nameclass = 'Galeria'
    producto = models.ForeignKey(Producto, blank=True, null=True, on_delete=models.CASCADE, related_name='producto_galeria')
    imagen = models.ImageField(upload_to=nombreArchivo, blank=True, null=True)
    nombre=models.CharField(max_length=25, blank=True, null=True)
    creado=models.DateTimeField(default=timezone.now)
    actualizado=models.DateTimeField(auto_now=True, blank=True, null=True)


    def __str__(self):
        return self.nombre








