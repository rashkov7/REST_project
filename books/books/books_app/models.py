from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()

class BookModel(models.Model):

    title = models.CharField(max_length=50)
    description = models.TextField(max_length=300, default="")
    pages = models.IntegerField(default=0)
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"
