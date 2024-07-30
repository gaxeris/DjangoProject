from rest_framework import serializers
from django.core.files import File
from django.core.files.storage import FileSystemStorage
from apps.users.models import User
from tasks.tasks import upload


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "image", "username"]


class UserImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "image"]
        extra_kwargs = {"partial": True}

    def update(self, instance, validated_data):
        image_file = self.context["image_file"]
        storage = FileSystemStorage()
        storage.save(image_file.name, File(image_file))

        return upload.delay(
            id=instance.pk,
            path=storage.path(image_file.name),
            file_name=image_file.name,
        )


class UserLoginSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}
