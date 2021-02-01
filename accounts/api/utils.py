from django.utils import timezone
from django.conf import settings
import datetime

from rest_framework_jwt.settings import api_settings

expires_delta = (api_settings.JWT_REFRESH_EXPIRATION_DELTA) - datetime.timedelta(seconds=200)

def jwt_response_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': user.username,
        'expires': timezone.now() + expires_delta
    }