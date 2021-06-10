from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework import permissions
from rest_framework.response import Response
# from dj_rest_auth.jwt_auth import JWTAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework
from usuario.models import User
from negocio.models import Negocio, Producto, CategoriaProducto, CategoriaNegocio,\
    Galeria
from usuario.permission import IsOwnerOrReadOnly, IsUserOrReadOnly
# from .serializers import PostSerializers, \
from negocio.serializers import NegocioNestedSerializer, ProductoNestedSerializer,CategoriaNegocioNestedSerializer,\
    CategoriaProductoNestedSerializer, ProductoNestedSerializer, GaleriaSerializers, CategoriaProductoSerializers, CategoriaNegocioSerializers
    # CatalogoNestedSerializer
from usuario.serializers import UsuarioSerializers
from .serializers import NegocioSerializers,  ProductoSerializers
    # ComentarioSerializers, \
    # ComentarioNegocioSerializers, \

    # UsuarioSerializers, \

#######################     CLASE PARA INHABILITAR EL CSRF TOKEN NO ES MUY BUENA IDEA PERO NO ENCUENTRO OTRA SOLUCION POR EL MOMENTO ############
from rest_framework.authentication import SessionAuthentication
class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening
#######################      ############

class ExtendedPagination(PageNumberPagination):
    page_size = 15

    def get_paginated_response(self, data):

        return Response({
            'count': self.page.paginator.count,
            'num_pages': self.page.paginator.num_pages,
            'page_number': self.page.number,
            'page_size': self.page_size,
            'next_link': self.get_next_link(),
            'previous_link': self.get_previous_link(),
            'results': data
        })



#Categorias con sus detalles para solo leer

class CategoriaNegocioReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [JWTAuthentication]
    queryset = CategoriaNegocio.objects.filter().order_by("-nombre","-id")
    serializer_class = CategoriaNegocioNestedSerializer

class CategoriaProductoReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [JWTAuthentication]
    queryset = CategoriaProducto.objects.filter().order_by("-nombre","-id")
    serializer_class = CategoriaProductoNestedSerializer


class NegocioReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Negocio.objects.filter(aprobado=True).order_by('-nombre', '-creado', '-actualizado')
    serializer_class = NegocioNestedSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    search_fields = ['nombre','descripcion','creado']
    ordering_fields =['creado', 'nombre']
    filterset_fields = {
        'creado': ['lte', 'gte'],  # Año menor o igual, mayor o igual que
        'nombre': ['exact'],  # Género exacto
        'categoria': ['exact']  # Género exacto
    }
    pagination_class = ExtendedPagination
    pagination_class.page_size = 10


class ProductoReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Producto.objects.filter(aprobado=True).order_by('-nombre', '-creado', '-actualizado')
    serializer_class = ProductoNestedSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    search_fields = ['nombre','descripcion','creado']
    ordering_fields =['creado', 'nombre']
    filterset_fields = {
        'creado': ['lte', 'gte'],  # Año menor o igual, mayor o igual que
        'nombre': ['exact'],  # Género exacto
        'categoria': ['exact']  # Género exacto
    }
    pagination_class = ExtendedPagination
    pagination_class.page_size = 10


#crear negocio, producto y galeria



class CategoriaNegocioViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    queryset = CategoriaNegocio.objects.filter().order_by("-nombre","-id")
    serializer_class = CategoriaNegocioSerializers

class CategoriaProductoViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = CategoriaProducto.objects.filter().order_by("-nombre","-id")
    serializer_class = CategoriaProductoSerializers




class NegocioViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Negocio.objects.filter(aprobado=True).order_by("-nombre", "-creado","-id")
    serializer_class = NegocioSerializers

class ProductoViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Producto.objects.filter(aprobado=True).order_by("-nombre", "-creado","-id")
    serializer_class = ProductoSerializers




class GaleriaViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Galeria.objects.filter().order_by("-creado","-id")
    serializer_class = GaleriaSerializers

