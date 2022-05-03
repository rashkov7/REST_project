from django.contrib import admin

from books.auth_app.models import BooksUser


@admin.register(BooksUser)
class AdminBooks(admin.ModelAdmin):
    pass