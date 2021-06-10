from rest_framework import serializers
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from usuario.models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed


class MyPasswordResetConfirmSerializer(serializers.Serializer):
    password=serializers.CharField(min_length=6, max_length=68, write_only=True)
    token=serializers.CharField(min_length=1, max_length=68, write_only=True)
    uidb64=serializers.CharField(min_length=1, write_only=True)

    class Meta:
        fields =['password','token','uidb64']


    def validate(self, attrs):

        try:
            password=attrs.get('password')
            token=attrs.get('token')
            uidb64=attrs.get('uidb64')
            id=force_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed('El enlace no es válido', 401)

            user.set_password(password)
            user.save()
        except Exception as e:
            raise AuthenticationFailed('El enlace no es válido', 401)

        return super().validate(attrs)