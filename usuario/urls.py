
from .apiviews import UsuarioViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path


router = DefaultRouter()
router.register('usuario', UsuarioViewSet, basename='usuario')

urlpatterns=[]

urlpatterns += router.urls



