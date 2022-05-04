from django.urls import path

from books.books_app.views import ListBookView, DetailsView, AuthorDashboardAPIView

urlpatterns = (
    path('books/', ListBookView.as_view(), name='books list'),
    path('books/<int:pk>', DetailsView.as_view(), name='book details'),
    path('dashboard/', AuthorDashboardAPIView.as_view(), name='user dashboard'),
)