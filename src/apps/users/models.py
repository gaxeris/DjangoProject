from django.db import models
from django.contrib.auth.models import AbstractUser

from utils.utils import user_self_directory_path

# Create your models here.


class User(AbstractUser):
    """Custom user model which replaces Django\`s auth.User and inherits the same behavior"""

    image = models.ImageField(
        upload_to=user_self_directory_path, width_field=100, height_field=100, null=True
    )

    class Meta:
        db_table = "auth_user"
