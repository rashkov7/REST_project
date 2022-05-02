from django.urls import path

from books.auth_app.views import RegisterAPIView

urlpatterns = (
    path('', RegisterAPIView.as_view(), name="register"),
)
