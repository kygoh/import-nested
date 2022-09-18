from django.contrib import admin
from import_export.admin import ImportMixin
from .models import Asset, Site, SiteAsset
from .resources import SiteResource

# Register your models here.
class SiteAdmin(ImportMixin, admin.ModelAdmin):
    resource_class = SiteResource

admin.site.register(Asset)
admin.site.register(Site, SiteAdmin)
admin.site.register(SiteAsset)
