
import random
import string
from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common.models import TimeStampedUUIDModel
from django.utils.text import slugify
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone

User = get_user_model()

# Create your models here.

class Sector(models.Model):
    title = models.CharField(verbose_name=_("Sector Title"),max_length=250)
    slug = AutoSlugField(populate_from = "title", unique=True,always_update=True)
    status = models.BooleanField(default=True)
    create_date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Sector"
        verbose_name_plural ="Sectors"

    def __str__(self):
        return self.title