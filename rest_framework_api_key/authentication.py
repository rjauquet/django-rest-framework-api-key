from rest_framework import authentication
from rest_framework import exceptions
from rest_framework_api_key.models import APIKey


class ApiKeyAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        api_key = request.META.get('HTTP_API_KEY', '')
        if not api_key:
            return None

        try:
            api_key = APIKey.objects.get(key=api_key)
        except APIKey.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such API key')

        return None, api_key
