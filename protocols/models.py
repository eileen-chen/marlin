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

    phase = models.CharField(max_length=30, verbose_name='Phase')
    display_name = models.CharField(max_length=50, verbose_name='Display Name')
    purpose = models.CharField(max_length=255, verbose_name='Purpose')
    
    #user = models.ForeignKey('User', on_delete=models.CASCADE)
    #color = models.IntegerField() How to use Enums for Django Field.choices
    approval_date = models.DateTimeField(verbose_name='Approval Date')
    start_date = models.DateTimeField(verbose_name='Start Date')
    end_date = models.DateTimeField(verbose_name='End Date')

    examine_number = models.CharField(max_length=100, verbose_name='Examine Number')
    protocol_number = models.CharField(max_length=100, verbose_name='Purpose')
    indications = models.CharField(max_length=100, verbose_name='Indication')
    category = models.EmailField(max_length=1, choices=CATEGORY_CHOICES, verbose_name='Category')

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Created Date')
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='Updated Date')

    auto_create_schema = True

    objects = models.Manager()

    REQUIRED_FIELDS = ['tenant_name', 'display_name']

    def __str__(self):
        return self.display_name


