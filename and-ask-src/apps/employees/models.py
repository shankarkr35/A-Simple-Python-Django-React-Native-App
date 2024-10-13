from django.db import models
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

class EmployeePublishedManager(models.Manager):
    def get_queryset(self):
        return (
            super(EmployeePublishedManager,self).get_queryset().filter(published_status=True)
        )

class Employee(models.Model):
    user = models.ForeignKey(User, verbose_name=_("Employee"),related_name="agent_name",on_delete=models.DO_NOTHING)
    name = models.CharField(verbose_name=_("Employee Name"),max_length=250)
    email = models.EmailField(verbose_name=_("Email Address"),max_length=255,unique=True)
    mobile_number = PhoneNumberField(verbose_name=_("Phone Number"),max_length=30,default="+91777771888")
    password = models.CharField(max_length=255,default="") 
    otp = models.CharField(max_length=15,default="")
    fcm_token = models.CharField(max_length=255,null=True)
    session_token = models.CharField(max_length=255,null=True)
    token_version = models.IntegerField(blank=True,null=True)
    status = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural ="Employees"

    def __str__(self):
        return self.name
