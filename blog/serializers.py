from rest_framework import serializers

from blog.models import Post, Comentario, Imagen, CategoriaPost
from usuario.models import User
from usuario.serializers import OwnerSerializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from datetime import timezone



class ComentarioSerializers(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    aprobado = serializers.HiddenField(default=False)
    class Meta:
        model=Comentario
        fields='__all__'



class CategoriaPostSerializers(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    aprobado = serializers.HiddenField(default=False)
    class Meta:
        model=CategoriaPost
        fields='__all__'



class PostSerializers(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    aprobado = serializers.HiddenField(default=False)
    class Meta:
        model=Post
        fields='__all__'


class ImagenSerializers(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    aprobado = serializers.HiddenField(default=False)
    class Meta:
        model=Imagen
        fields='__all__'


class PostNestedSerializer(WritableNestedModelSerializer):
    owner = OwnerSerializers(allow_null=True)
    aprobado = serializers.HiddenField(default=False)
    categoria = CategoriaPostSerializers(many=True)
    post_comentario = ComentarioSerializers(many=True)
    post_imagen = ImagenSerializers(many=True)

    class Meta:
        model=Post
        fields='__all__'

class PostUserNestedSerializer(WritableNestedModelSerializer):
    owner = OwnerSerializers(allow_null=True)
    aprobado = serializers.HiddenField(default=False)
    categoria = CategoriaPostSerializers(many=True)
    post_comentario = ComentarioSerializers(many=True)

    class Meta:
        model=Post
        fields='__all__'

class CategoriaPostNestedSerializer(WritableNestedModelSerializer):

    categoria_post = PostUserNestedSerializer(many=True)

    class Meta:
        model=CategoriaPost
        fields='__all__'


