from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import Site, Asset, SiteAsset
from .widgets import CustomForeignKeyWidget

class SiteResource(resources.ModelResource):

    class Meta:
        model = Site

class AssetResource(resources.ModelResource):
    parent = fields.Field(attribute='parent', column_name='parent', widget=ForeignKeyWidget(model=Asset, field='code'))

    class Meta:
        model = Asset

class SiteAssetResource(resources.ModelResource):
    site = fields.Field(attribute='site', column_name='site', widget=ForeignKeyWidget(model=Site, field='site_no'))
    asset = fields.Field(attribute='asset', column_name='asset', widget=ForeignKeyWidget(model=Asset, field='code'))
    parent = fields.Field(attribute='parent', column_name='parent', widget=ForeignKeyWidget(model=SiteAsset, field='reference'))

    class Meta:
        model = SiteAsset
