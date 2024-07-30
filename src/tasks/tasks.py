from time import sleep
from celery import shared_task

from django.core.files import File
from django.core.files.storage import FileSystemStorage
from pathlib import Path

from apps.users.models import User


@shared_task
def upload(id, path, file_name):

    storage = FileSystemStorage()
    path_object = Path(path)
    with path_object.open(mode="rb") as file:
        picture = File(file, name=path_object.name)

        instance = User.objects.get(pk=id)
        instance.image = picture
        instance.save(update_fields=["image"])

    storage.delete(file_name)
