from rest_framework import serializers

from usuario.models import User


class UsuarioSerializers(serializers.ModelSerializer):
    email = serializers.ReadOnlyField()
    username = serializers.ReadOnlyField()
    class Meta:
        model=User
        fields=[
            'id',
            'username',
            'first_name',
            'last_name',
            'date_joined',
            'email',
            'uid',
            'amigos'

        ]

class OwnerSerializers(serializers.ModelSerializer):

    aprobado = serializers.HiddenField(default=False)
    class Meta:
        model=User
        fields=["id","email","username","first_name","last_name","aprobado"]


