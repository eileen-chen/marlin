import uuid
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class User(models.Model):

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
        return self.email

class Profile(models.Model):

    first_name = models.CharField(max_length=30, null=True, blank=True)
    middle_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    avatar = models.ImageField(null=True, blank=True)
    identity_number = models.CharField(max_length=30, db_index=True, null=True, blank=True)
    identity_country = models.CharField(max_length=30, null=True, blank=True)
    #user = models.ForeignKey('User', on_delete=models.CASCADE)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

class Demography(models.Model):

    # Enums
    GENDER_CHOICES = (
        ('0', 'Male'),
        ('1', 'Female'),
        ('2', 'Unknow'),
    )

    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    height = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    country = models.CharField(max_length=30, null=True, blank=True)
    state_code = models.CharField(max_length=10, null=True, blank=True)
    postal_code = models.CharField(max_length=10, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    alternate_address = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    alternate_phone = models.CharField(max_length=30, null=True, blank=True)
    race = models.CharField(max_length=30, null=True, blank=True)
    ethnicity = models.CharField(max_length=30, null=True, blank=True)
    #user = models.ForeignKey('User', on_delete=models.CASCADE)

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    # def __str__(self):
    #     return self.identity_number

    # class Meta:
    #     verbose_name = _('user')
    #     verbose_name_plural = _('users')
    #
    # def gte_absolute_url(self):
    #     return "/users/%s/" % urlquote(self.email)

    # def get_full_name(self):
    #     """
    #     Returns the first_name plus the last_name, with a space in between.
    #     """
    #     full_name = '%s %s' % (self.first_name, self.last_name)
    #     return full_name.strip()

    # def get_short_name(self):
    #     "Returns the short name for the user."
    #     return self.first_name

    # def email_user(self, subject, message, from_email=None):
    #     """
    #     Sends an email to this User.
    #     """
    #     send_mail(subject, message, from_email, [self.email])

# Create your models here.
# class UserManager(BaseUserManager):
#     def _create_user(self, email, password, **extra_fields):
#         """
#         Creates and saves a User with the given email and password.
#         """
#         now = timezone.now()
#         if not email:
#             raise ValueError('The given email must be set')
#
#         email = self.normalize_email(email)
#         user = self.model(email=email,
#                           is_active=True,
#                           last_login=now,
#                           date_joined=now,
#                           **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_user(self, email, password, **extra_fields):
#
#          return self._create_user(email, password, **extra_fields)
