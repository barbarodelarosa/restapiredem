from rest_framework import serializers

from rest_framework.authtoken.models import Token
from negocio.models import CategoriaProducto, CategoriaNegocio, Negocio, Producto,\
    Seguidor, Galeria

from usuario.models import User
from usuario.serializers import OwnerSerializers
from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from drf_writable_nested.serializers import WritableNestedModelSerializer






class SeguidorSerializers(serializers.ModelSerializer):
      class Meta:
        model=Seguidor
        fields='__all__'

class CategoriaNegocioSerializers(serializers.ModelSerializer):
    class Meta:
        model=CategoriaNegocio
        fields='__all__'


class NegocioSerializers(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    aprobado = serializers.HiddenField(default=False)
    class Meta:
        model=Negocio
        fields='__all__'


class CategoriaProductoSerializers(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    aprobado = serializers.HiddenField(default=False)
    class Meta:
        model=CategoriaProducto
        fields='__all__'


class ProductoSerializers(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    aprobado = serializers.HiddenField(default=False)
    class Meta:
        model=Producto
        fields='__all__'




class GaleriaSerializers(serializers.ModelSerializer):
    class Meta:
        model=Galeria
        fields='__all__'



"""
/////////////////////////////////  NESTEDMODELSSERIALIZERS  //////////////////////////////////
"""


class NegocioNestedSerializer(WritableNestedModelSerializer):
    owner = OwnerSerializers(allow_null=True)
    aprobado = serializers.HiddenField(default=False)
    productos=ProductoSerializers(many=True)
    # empleados = EmpleadoSerializers(many=True)
    seguidores = SeguidorSerializers(many=True)
    categoria = CategoriaNegocioSerializers(allow_null=True)

    class Meta:
        model=Negocio
        fields='__all__'


class CategoriaNegocioNestedSerializer(WritableNestedModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    aprobado = serializers.HiddenField(default=False)
    categoria_negocio = NegocioNestedSerializer(many=True)
    class Meta:
        model=CategoriaNegocio
        fields='__all__'



class CategoriaProductoNestedSerializer(WritableNestedModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    aprobado = serializers.HiddenField(default=False)
    categoria_producto = ProductoSerializers(many=True)
    class Meta:
        model=CategoriaProducto
        fields='__all__'


class ProductoNestedSerializer(WritableNestedModelSerializer):
    owner = OwnerSerializers(allow_null=True)
    aprobado = serializers.HiddenField(default=False)
    categoria = CategoriaProductoSerializers(allow_null=True)
    negocio = NegocioSerializers(allow_null=True)
    # comentarios_producto = ComentarioProductoSerializers(many=True)
    class Meta:
        model=Producto
        fields='__all__'


