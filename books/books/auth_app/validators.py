from rest_framework import serializers


def passwords_mach_validate(pass1,pass2):
    if pass1 == pass2:
        return None
    raise serializers.ValidationError({"password2": 'Passwords must match !'})

