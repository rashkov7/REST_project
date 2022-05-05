from django.urls import path

from books.profile_app.views import ProfileAPIView


urlpatterns = (
    path("<int:pk>/", ProfileAPIView.as_view(), name="profile"),
)
