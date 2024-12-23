from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from sites.models import APIKey  # Замените на вашу модель

class APIKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        api_key = request.headers.get('X-API-KEY')
        if not api_key:
            return None

        try:
            api_key_obj = APIKey.objects.get(key=api_key)
            return (api_key_obj.user, None)
        except APIKey.DoesNotExist:
            raise AuthenticationFailed('Invalid API key')