from django.contrib import admin

from books.profile_app.models import ProfileModel


@admin.register(ProfileModel)
class AdminProfile(admin.ModelAdmin):
    pass