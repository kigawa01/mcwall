# Create your models here.
import uuid

from django.db import models
from django.utils import timezone


class ImageModel(models.Model):
    uid = models.UUIDField(primary_key=True, editable=False,default=uuid.uuid4)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=1024, blank=True)
    file = models.ImageField()
    created_at = models.DateTimeField(editable=False, default=timezone.now)
