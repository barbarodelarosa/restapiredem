
from usuario.apiviews import UsuarioViewSet
from blog.apiviews import CategoriaPostViewSet, PostViewSet, ComentarioPostViewSet, CategoriaPostReadOnlyModelViewSet, \
                          PostReadOnlyModelViewSet, ImagenPostViewSet

from negocio.apiviews import CategoriaProductoReadOnlyModelViewSet, \
                             CategoriaNegocioReadOnlyModelViewSet, NegocioViewSet, \
                             NegocioReadOnlyModelViewSet, ProductoViewSet, ProductoReadOnlyModelViewSet, GaleriaViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path


router = DefaultRouter()
router.register('categoria-post', CategoriaPostReadOnlyModelViewSet, basename='categoria-post')
router.register('create-post', PostViewSet, basename='create-post')
router.register('read-post', PostReadOnlyModelViewSet, basename='read-post')
router.register('comentario-post', ComentarioPostViewSet, basename='comentario-post')
router.register('imagen', ImagenPostViewSet, basename='imagen')

router.register('categoria-negocio', CategoriaNegocioReadOnlyModelViewSet, basename='categoria-negocio')
router.register('categoria-producto', CategoriaProductoReadOnlyModelViewSet, basename='categoria-producto')
router.register('create-negocio', NegocioViewSet, basename='create-negocio')
router.register('read-negocio', NegocioReadOnlyModelViewSet, basename='read-negocio')
router.register('create-producto', ProductoViewSet, basename='create-producto')
router.register('read-producto', ProductoReadOnlyModelViewSet, basename='read-producto')
router.register('galeria', GaleriaViewSet, basename='read-producto')



router.register('usuario', UsuarioViewSet, basename='usuario')

urlpatterns=[

]

urlpatterns += router.urls



