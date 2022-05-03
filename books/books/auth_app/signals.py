from django.db.models import signals
from django.dispatch import receiver

from books.auth_app.models import BooksUser
from books.profile_app.models import ProfileModel


@receiver(signals.post_save, sender=BooksUser)
def user_created(instance, created,**kwargs):
    if created:
        profile = ProfileModel.objects.create(
            first_name="Anonymous",
            last_name="Anonymous",
            user=instance
        )

