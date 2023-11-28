import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class AppUser(AbstractUser):
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)

