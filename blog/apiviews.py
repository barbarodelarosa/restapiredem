from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
# from dj_rest_auth.jwt_auth import JWTAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

from blog.models import Post,CategoriaPost, Comentario, Imagen

from usuario.permission import IsOwnerOrReadOnly
from blog.serializers import PostNestedSerializer, CategoriaPostNestedSerializer, ComentarioSerializers,\
    CategoriaPostSerializers, PostSerializers, ImagenSerializers



class ExtendedPagination(PageNumberPagination):
    page_size = 10

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



class PostViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.filter(aprobado=True)
    serializer_class = PostSerializers


class PostReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [JWTAuthentication]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.filter(aprobado=True).order_by('-creado','-actualizado')
    serializer_class = PostNestedSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    search_fields = ['titulo','mensaje','creado']
    ordering_fields =['creado', 'titulo']
    filterset_fields = {
        'creado': ['lte', 'gte'],  # Año menor o igual, mayor o igual que
        'titulo': ['exact'],  # Género exacto
        'categoria': ['exact']  # Género exacto
    }
    pagination_class = ExtendedPagination
    pagination_class.page_size = 10


class CategoriaPostViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = CategoriaPost.objects.filter().order_by("-nombre","-id")
    serializer_class = CategoriaPostNestedSerializer

class CategoriaPostReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = CategoriaPost.objects.filter().order_by("-nombre","-id")
    serializer_class = CategoriaPostNestedSerializer

class ComentarioPostViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Comentario.objects.filter(aprobado=True).order_by("-creado","-id")
    serializer_class = ComentarioSerializers

class ImagenPostViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Imagen.objects.filter().order_by("-creado","-id")
    serializer_class = ImagenSerializers
#
# class ComentarioPostViewSet(viewsets.ModelViewSet):
#     authentication_classes = ()
#     # authentication_classes = [JWTAuthentication]
#     # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
#     permission_classes = ()
#     queryset = Comentario.objects.filter(aprobado=True).order_by("-creado","-id")
#     serializer_class = ComentarioPostNestedSerializer


