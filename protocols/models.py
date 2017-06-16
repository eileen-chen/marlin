from django.db import models
from django.utils import timezone
from tenant_schemas.models import TenantMixin


# Create your models here.
class Protocol(TenantMixin):

    # Enums
    CATEGORY_CHOICES = (
        ('0', 'Single Center'),
        ('1', 'Multicenter'),
    )

    phase = models.CharField(max_length=30)
    display_name = models.CharField(max_length=50)
    tenant_name = models.CharField(max_length=30)
    #color = models.IntegerField() How to use Enums for Django Field.choices
    description = models.CharField(max_length=255)
    #user = models.ForeignKey('User', on_delete=models.CASCADE)

    approval_date = models.DateTimeField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    examine_number = models.CharField(max_length=100)
    protocol_number = models.CharField(max_length=100)
    purpose = models.CharField(max_length=255)
    indications = models.CharField(max_length=100)
    category = models.EmailField(max_length=1, choices=CATEGORY_CHOICES)

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    auto_create_schema = True

    objects = models.Manager()

    REQUIRED_FIELDS = ['tenant_name', 'display_name']

    def __str__(self):
        return self.display_name
