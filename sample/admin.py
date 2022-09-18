from django.contrib import admin
from import_export.admin import ImportMixin
from .models import Asset, Site, SiteAsset
from .resources import SiteResource, AssetResource

# Register your models here.
class SiteAdmin(ImportMixin, admin.ModelAdmin):
    resource_class = SiteResource

class AssetAdmin(ImportMixin, admin.ModelAdmin):
    resource_class = AssetResource

admin.site.register(Asset, AssetAdmin)
admin.site.register(Site, SiteAdmin)
admin.site.register(SiteAsset)
