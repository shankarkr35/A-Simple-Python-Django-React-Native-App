from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from apps.common.models import TimeStampedUUIDModel

User = get_user_model()

class Gender(models.TextChoices):
    MALE = 'Male',_("Male")
    FEMALE = 'Female',_("Female")
    OTHER = 'Other',_("Other")

class Profile(TimeStampedUUIDModel):
    user = models.OneToOneField(User,related_name="profile",on_delete=models.CASCADE)
    phone_number = PhoneNumberField(verbose_name=_("Phone Number"),max_length=30,default="+917717720891")
    about_me = models.TextField(verbose_name=_("About Me"), default="Say something about your self")
    profile_photo = models.ImageField(verbose_name=_("Profile Photo"),default='/profile_default.png')
    gender = models.CharField(verbose_name=_("Gender"),choices=Gender.choices, default=Gender.OTHER, max_length=20)

    def __str__(self):
        return f"{self.user.username}'s profile"