
from blog import apiviews
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
# router.register('categoria', apiviews.CategoriaPostViewSet, basename='categoria-post')
router.register('post', apiviews.PostNestedSerializer, basename='post')
router.register('comentario', apiviews.ComentarioPostViewSet, basename='comentario-post')
# router.register('galeria', apiviews.GaleriaViewSet, basename='galeria')

urlpatterns=[

]

urlpatterns += router.urls



