from django.contrib.auth import get_user_model
from rest_framework import response, status
from rest_framework.authtoken import views as auth_views

from rest_framework.views import APIView

from books.auth_app.serializers import BooksUserSerializer

UserModel = get_user_model()


class RegisterAPIView(APIView):

    serializer_class = BooksUserSerializer

    def get(self, request):
        users = UserModel.objects.all()
        serializer = self.serializer_class(users, many=True)
        return response.Response({"all registered users": serializer.data})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class LoginAPIVIew(auth_views.ObtainAuthToken):
    pass