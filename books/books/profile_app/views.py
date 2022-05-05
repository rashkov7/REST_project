from django.contrib.auth import get_user_model
from rest_framework import generics, permissions

from books.auth_app.models import BooksUser
from books.profile_app.models import ProfileModel
from books.profile_app.serializers import ProfileSerializer

UserModel = get_user_model()

class ProfileAPIView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProfileSerializer
    queryset = ProfileModel.objects.all()


