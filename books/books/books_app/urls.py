from django.urls import path

from books.books_app.views import ListBookView, DetailsView, AuthorDashboardAPIView, DetailsAPIView

urlpatterns = (
    path('books/', ListBookView.as_view(), name='books list'),
    path('<int:pk>', DetailsView.as_view(), name='book details'),
    path('generic/<int:id>', DetailsAPIView.as_view(), name='details'),
    path('dashboard/', AuthorDashboardAPIView.as_view(), name='user dashboard'),
)