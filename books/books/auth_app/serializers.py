from django.contrib.auth import get_user_model
from rest_framework import serializers

from books.auth_app.validators import passwords_mach_validate

UserModel = get_user_model()


class BooksUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=50,
        min_length=6,
        write_only=True,
        style={"input_type":"password"})
    password2 = serializers.CharField(
        max_length=50,
        min_length=6,
        write_only=True,
        style={"input_type":"password"})

    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD, 'password', 'password2')

    def validate(self, attrs):
        pass1 = attrs['password']
        pass2 = attrs['password2']
        passwords_mach_validate(pass1, pass2)
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        return UserModel.objects.create_user(**validated_data)
