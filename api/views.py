from django.shortcuts import render
from rest_framework import generics, status, views
from usuario.models import User
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import *
from rest_framework.response import Response
from django.urls import reverse
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from api.serializers import MyPasswordResetConfirmSerializer

from dj_rest_auth.app_settings import PasswordResetConfirmSerializer
    # JWTSerializer, JWTSerializerWithExpiration, LoginSerializer,
    # PasswordChangeSerializer, ,
class MyPasswordTokenCheckAPI(generics.GenericAPIView):
    def get(self, request, uidb64, token):
        try:
            id=smart_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({'error': 'El token utilizado no es válido'}, status=status.HTTP_401_UNAUTHORIZED)

            return Response({'success':True, 'message':'Credencial Valid','uidb64':uidb64,'token':token}, status=status.HTTP_200_OK)


        except DjangoUnicodeDecodeError as identifier:
            if not PasswordResetTokenGenerator().check_token(user):
                return Response({'error':'El token utilizado no es válido'},status=status.HTTP_401_UNAUTHORIZED)


class MySetNewPasswordAPIView(generics.GenericAPIView):
    serializer_class = MyPasswordResetConfirmSerializer

    def patch(self, request):
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({
            'success': True,
            'message':'La contraseña ha sido modificada'
        }, status=status.HTTP_200_OK)