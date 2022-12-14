from django.db import models

class Asset(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a descriptive name for this asset')
    code = models.CharField(max_length=80, help_text='Enter a code that will be used to reference this asset')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        """String for representing the Model object."""
        if self.parent is None:
            return self.name
        else:
            return str(self.parent) + ' > ' + self.name

class Site(models.Model):
    site_no = models.CharField("Site Number", max_length=255)
    name = models.CharField("Site name", max_length=100)

    def __str__(self):
        return self.name

class SiteAsset(models.Model):
    site = models.ForeignKey("Site", on_delete=models.CASCADE)
    asset = models.ForeignKey("Asset", on_delete=models.CASCADE)
    reference = models.CharField(max_length=200, help_text='Enter a reference for this asset on site')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        """String for representing the Model object."""
        return '%s: %s @ %s' % (self.reference, str(self.asset), self.site.name)
