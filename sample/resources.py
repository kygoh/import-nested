from import_export import resources, fields
from .models import Site

class SiteResource(resources.ModelResource):

    class Meta:
        model = Site