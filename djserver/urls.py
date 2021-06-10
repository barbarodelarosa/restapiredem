"""redem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


from dj_rest_auth.registration.views import RegisterView, VerifyEmailView, ConfirmEmailView
from dj_rest_auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView, UserDetailsView,\
    PasswordChangeView
from rest_framework_simplejwt.views import  TokenObtainPairView,  TokenRefreshView, TokenVerifyView




from api.views import MyPasswordTokenCheckAPI, MySetNewPasswordAPIView









urlpatterns = [

    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),



    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('schema', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),



    path('api/auth/account-confirm-email/<str:key>/', ConfirmEmailView.as_view()),
    path('api/auth/register/', RegisterView.as_view()),
    path('api/auth/login/', LoginView.as_view()),
    path('api/auth/user/', UserDetailsView.as_view()),
    path('api/auth/logout/', LogoutView.as_view()),




    path('api/auth/password-change/', PasswordChangeView.as_view()),
    path('api/auth/password-reset/', PasswordResetView.as_view()),
    path('api/auth/password-reset-confirm/<uidb64>/<token>/',MyPasswordTokenCheckAPI.as_view(), name='password_reset_confirm'),
    path('api/auth/password-reset-complete/',MySetNewPasswordAPIView.as_view(), name='password_reset_complete'),
    # path('api/auth/password-reset-confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('api/auth/verify-email/', VerifyEmailView.as_view(), name='rest_verify_email'),
    path('api/auth/account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    re_path(r'^api/auth/account-confirm-email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(), name='account_confirm_email'),





]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



