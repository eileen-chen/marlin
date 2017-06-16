from protocols.models import Protocol
from django.utils import timezone
import logging

try:
    is_exist = Protocol.objects.filter(schema_name='public').exists()
    if not is_exist:
        Protocol(domain_url='localhost', schema_name='public',
                 tenant_name='public', description='public tenant schema',
                 approval_date=timezone.now(), start_date=timezone.now(),
                 end_date=timezone.now()).save()
    else:
        print('public schema is exist!')
except:
    pass

# try:
#     protocol = Protocol.objects.get(schema_name='public')
# except ObjectDoesNotExist:
#     print('public schema is not exist!')
    # Protocol(domain_url='localhost', schema_name='public',
    #          tenant_name='public', description='public tenant schema',
    #          approval_date=timezone.now(), start_date=timezone.now(),
    #          end_date=timezone.now()).save()
