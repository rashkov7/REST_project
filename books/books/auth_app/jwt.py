from rest_framework import exceptions
from rest_framework.authentication import get_authorization_header, BaseAuthentication
import jwt
from django.conf import settings

from books.auth_app.models import BooksUser


class JWTAuthentication(BaseAuthentication):

    def authenticate(self, request):
        auth_headers = get_authorization_header(request)
        auth_data = auth_headers.decode('utf-8')
        auth_token = auth_data.split(" ")

        if not len(auth_token) == 2:
            raise exceptions.AuthenticationFailed('Token not valid')
        token = auth_token[1]

        try:

            payload =jwt.decode(token, settings.SECRET_KEY, algorithms="HS256")
            email = payload['email']
            user = BooksUser.objects.get(email=email)
            return user, token

        except jwt.ExpiredSignatureError as ex:
            raise exceptions.AuthenticationFailed('Token is expired')

        except jwt.DecodeError as ex:
            raise exceptions.AuthenticationFailed('Token is invalid')

        except BooksUser.DoesNotExist as no_user:
            raise exceptions.AuthenticationFailed('No such User.')
