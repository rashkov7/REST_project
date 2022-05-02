from django.urls import path

from books.auth_app.views import RegisterAPIView,LoginAPIVIew

urlpatterns = (
    path('auth/', RegisterAPIView.as_view(), name="register"),
    path('login/', LoginAPIVIew.as_view(), name="login"),
)
