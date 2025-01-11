from django.apps import AppConfig
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        User = get_user_model()
        post_save.connect(self.create_user_profile, sender=User)

    def create_user_profile(self, sender, instance, created, **kwargs):
        from .models import UserProfile  # Moved import back here
        if created:
            UserProfile.objects.create(user=instance)
