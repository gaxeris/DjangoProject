from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfile(models.Model):

    user_name = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):  
        return str(self.user_name)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user_name=instance)

post_save.connect(create_user_profile, sender=User)