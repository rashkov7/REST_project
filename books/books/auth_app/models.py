import datetime

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User, PermissionsMixin
from django.db import models

from books.auth_app.managers import BooksUserManager


class BooksUser(AbstractBaseUser, PermissionsMixin):
    """
    Email and password are required. Other fields are optional.
    """
    email = models.EmailField(
        "email address",
        unique=True,
        error_messages={
        "unique": "A user with that username already exists."
    })
    is_staff = models.BooleanField(
        "staff status",
        default=False,
        help_text="Designates whether the user can log into this admin site.",
    )
    is_active = models.BooleanField(
        "active",
        default=True,
        help_text=(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField("date joined", auto_now_add=datetime.datetime.now())

    objects = BooksUserManager()

    USERNAME_FIELD = "email"

