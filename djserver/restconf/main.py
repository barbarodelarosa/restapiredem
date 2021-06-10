import datetime
import os
from dotenv import load_dotenv
load_dotenv()
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        #'rest_framework.authentication.BasicAuthentication',

        # 'rest_framework_simplejwt.authentication.JSONWebTokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        # 'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
        'rest_framework.authentication.SessionAuthentication', #Oauth, JWT


    ),
    # 'DEFAULT_PERMISSION_CLASSES': (
    #     'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    # ),
    'DEFAULT_PAGINATION_CLASS': 'djserver.restconf.pagination.CFEAPIPagination',
    'DEFAULT_FILTER_BACKENDS': (
            'rest_framework.filters.SearchFilter',
            'rest_framework.filters.OrderingFilter',
    ),
    'SEARCH_PARAM': 'q',
    'ORDERING_PARAM': 'ordering',
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}



JWT_AUTH = {
    'JWT_ENCODE_HANDLER':
    'rest_framework_jwt.utils.jwt_encode_handler',

    'JWT_DECODE_HANDLER':
    'rest_framework_jwt.utils.jwt_decode_handler',

    'JWT_PAYLOAD_HANDLER':
    'rest_framework_jwt.utils.jwt_payload_handler',

    'JWT_PAYLOAD_GET_USER_ID_HANDLER':
    'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',

    'JWT_RESPONSE_PAYLOAD_HANDLER':
    #'rest_framework_jwt.utils.jwt_response_payload_handler'
    'accounts.api.utils.jwt_response_payload_handler',

    'JWT_ALLOW_REFRESH': True,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),

    'JWT_AUTH_HEADER_PREFIX': 'JWT', # Authorization: JWT <token>
    'JWT_AUTH_COOKIE': None,

}
REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER':'usuario.serializers.UsuarioSerializers',
}
OLD_PASSWORD_FIELD_ENABLED = True
LOGOUT_ON_PASSWORD_CHANGE = False

AUTHENTICATION_BACKENDS = [
    'allauth.account.auth_backends.AuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
]
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_CONFIRM_EMAIL_ON_GET = True

LOGIN_URL = os.getenv('LOGIN_URL')
REST_USE_JWT = True
# ACCOUNT_EMAIL_VERIFICATION = 'none'

EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
# EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'


