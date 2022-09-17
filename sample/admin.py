from django.contrib import admin
from .models import Asset, Site, SiteAsset

# Register your models here.
admin.site.register(Asset)
admin.site.register(Site)
admin.site.register(SiteAsset)
