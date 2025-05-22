# authentication.py

from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import APIKey

class APIKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        key = request.headers.get("X-API-Key")
        if not key:
            raise AuthenticationFailed("API key required")

        try:
            api_key = APIKey.objects.select_related('user').get(key=key, is_active=True)
        except APIKey.DoesNotExist:
            raise AuthenticationFailed("Invalid or inactive API key")

        # 認証ユーザーを返す
        return (api_key.user, api_key)
