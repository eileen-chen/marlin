from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.db import connection
from django.http import Http404
from tenant_schemas.utils import get_tenant_model, get_public_schema_name
from django.db import utils


class TenantTutorialMiddleware(object):
    def __init__(self):
        self.filter_first_path = ['account']

    def process_request(self, request): # Wei-Lin
        connection.set_schema_to_public()
        hostname_without_port = filter_url_path(request.path)

        if hostname_without_port in self.filter_first_path:
            print("public schema")
        else:

            TenantModel = get_tenant_model()

            try:
                request.tenant = TenantModel.objects.get(schema_name=hostname_without_port)
            except utils.DatabaseError:
                request.urlconf = settings.PUBLIC_SCHEMA_URLCONF
                return
            except TenantModel.DoesNotExist:
                if hostname_without_port in ("127.0.0.1", "localhost"):
                    request.urlconf = settings.PUBLIC_SCHEMA_URLCONF
                    return
                else:
                    raise Http404

            connection.set_tenant(request.tenant)
        ContentType.objects.clear_cache()

        if hasattr(settings, 'PUBLIC_SCHEMA_URLCONF') and request.tenant.schema_name == get_public_schema_name():
            request.urlconf = settings.PUBLIC_SCHEMA_URLCONF

def filter_url_path(path):
    """
    Filter url from the address. Only for
    routing purposes. www.test.com/teant1/ and www.test.com/teant2/ should
    find the different tenant.
    """
    if path:
        _first_path = list(filter(None, path.split('/')))
        return _first_path[0]