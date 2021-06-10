from blog.apiviews import CategoriaPostNestedSerializer, PostNestedSerializer, ComentarioPostViewSet
from usuario.apiviews import UsuarioViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('usuario', UsuarioViewSet, basename='usuario')
router.register('categoria-post', CategoriaPostNestedSerializer, basename='categoria-post')
router.register('post', PostNestedSerializer, basename='post')
router.register('comentario-post', ComentarioPostViewSet, basename='comentario-post')
# router.register('galeria', apiviews.GaleriaViewSet, basename='galeria')


urlpatterns=[]
urlpatterns += router.urls
