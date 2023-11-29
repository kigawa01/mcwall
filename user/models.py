import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.db import models


class AppUserManager(UserManager):
    pass


class AppUser(AbstractBaseUser):
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    username = models.CharField(max_length=150, blank=False, unique=True)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    objects = AppUserManager()
