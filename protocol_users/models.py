from django.db import models
from django.utils import timezone

#Create your models here.
class ProtocolUser(models.Model):

    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    avatar = models.ImageField()
    identity_number = models.CharField(max_length=30, db_index=True)
    identity_country = models.CharField(max_length=30)

    objects = models.Manager()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


# Create your models here.
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
    address = models.CharField(max_length=50)
    alternate_address = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)
    alternate_phone = models.CharField(max_length=30)
    race = models.CharField(max_length=30)
    ethnicity = models.CharField(max_length=30)
    mrn = models.CharField(max_length=30)
    external_id = models.CharField(max_length=30)
    diagnosis = models.CharField(max_length=30)
    site_name = models.CharField(max_length=30)
    site_code = models.CharField(max_length=30)

    protocol_user = models.OneToOneField(
        ProtocolUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )


class Role(models.Model):

    # Enums
    ROLE_CHOICES = (
        ('0', 'Principal Investigator'),
        ('1', 'Doctor'),
        ('2', 'Nurse Researcher'),
        ('3', 'Clinical Researcher Associate'),
        ('4', 'Pharmacist'),
        ('5', 'Site'),
    )

    display_name = models.EmailField(max_length=1, unique=True, choices=ROLE_CHOICES)
    abbreviation = models.CharField(max_length=30)

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    protocol_user = models.ForeignKey('ProtocolUser', on_delete=models.CASCADE)

    objects = models.Manager()

    REQUIRED_FIELDS = ['abbreviation', 'display_name']

    def __str__(self):
        return self.display_name
