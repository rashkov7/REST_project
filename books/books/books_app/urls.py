from django.urls import path

from books.books_app.views import ListBookView

urlpatterns = (
    path('books/', ListBookView.as_view(), name='books list'),
)