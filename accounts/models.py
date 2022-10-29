import os

from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.files.storage import FileSystemStorage
from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=60, null=False, blank=False)

    def __str__(self):
        return self.name


class UserManager(BaseUserManager):
    def create_user(self, email, password, first_name=None, last_name=None, **extra_fields):
        if not email:
            raise ValueError('Enter an email address')
        if not first_name:
            raise ValueError('Enter a first name')
        if not last_name:
            raise ValueError('Enter a last name')
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, first_name, last_name):
        user = self.create_user(email, password=password, first_name=first_name, last_name=last_name)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class ImageAvatarStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        # file must have the same extension as the file saved in database
        # files avatar_1.jpg and avatar_1.jpeg are different files
        if self.exists(name):
            os.remove(os.path.join(settings.BASE_DIR, name))
        return name


def avatar_path(instance, filename):
    ext = filename.split('.')[-1]
    return f'images/avatars/avatar_{instance.pk}.{ext}'


class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=150)
    country = models.ForeignKey('Country', on_delete=models.PROTECT, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    street = models.CharField(max_length=150, null=True, blank=True)
    zip_code = models.CharField(max_length=10, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    avatar = models.ImageField(upload_to=avatar_path, storage=ImageAvatarStorage(), null=True, blank=True)
    communication_channel = models.CharField(max_length=150, null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    # avoid username field
    username = None

    objects = UserManager()

