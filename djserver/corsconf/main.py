
# CORS HEADERS ENBALED
CORS_URLS_REGEX = r'^/api/.*$'
# CORS_ORIGIN_WHITELIST = (
#     'http://localhost:8100',
#     'http://127.0.0.1:8100'
# )
CORS_ORIGIN_ALLOW_ALL = True

from corsheaders.defaults import default_headers

CORS_ALLOW_HEADERS = default_headers + (
    'X-CSRFToken',
)

CORS_ALLOW_CREDENTIALS = True

