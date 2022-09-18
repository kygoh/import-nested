from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import Site, Asset

class SiteResource(resources.ModelResource):

    class Meta:
        model = Site

class AssetResource(resources.ModelResource):
    parent = fields.Field(attribute='parent', column_name='parent', widget=ForeignKeyWidget(model=Asset, field='code'))

    class Meta:
        model = Asset
