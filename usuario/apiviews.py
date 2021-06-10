# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets, filters
# from rest_framework.pagination import PageNumberPagination
from rest_framework import permissions
# from rest_framework.response import Response
# from dj_rest_auth.jwt_auth import JWTAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from usuario.models import User

from .permission import IsUserOrReadOnly

from usuario.serializers import UsuarioSerializers



class UsuarioViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UsuarioSerializers




