from django.db import models
from .user import User
from django.contrib.auth.models import AbstractBaseUser


class Profile(AbstractBaseUser):

    first_name = models.CharField(max_length=30, null=True, blank=True)
    middle_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    avatar = models.ImageField(null=True, blank=True)
    identity_number = models.CharField(max_length=30, null=True, blank=True)
    identity_country = models.CharField(max_length=30, null=True, blank=True)

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )