from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    """Custom user model which replaces Django\`s auth.User and has the same behavior"""

    class Meta:
        db_table = "auth_user"
