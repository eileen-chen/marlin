import uuid

from django.db import models
#from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class User(AbstractBaseUser):

    # User field
    email = models.EmailField(max_length=100, unique=True, db_index=True)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True,
        help_text = _('Designates whether this user should be treated as '
                      'active. Unselect this instead of deleting accounts.'))
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    # Confirmation field
    confirmation_token = models.CharField(max_length=100, default=uuid.uuid4)
    confirmation_at = models.DateTimeField(null=True, blank=True)

    objects = models.Manager()
    REQUIRED_FIELDS = ['email', 'password']

    def __str__(self):
        return '%s %s' % (self.email, self.is_active)