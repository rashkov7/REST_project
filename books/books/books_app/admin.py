from django.contrib import admin

from books.books_app.models import BookModel


@admin.register(BookModel)
class AdminBookModel(admin.ModelAdmin):
    pass