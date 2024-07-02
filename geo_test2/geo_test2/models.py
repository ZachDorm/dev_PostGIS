from django.contrib.gis.db import models
from django.contrib.gis import forms
from django.contrib.gis.forms.widgets import OSMWidget

class States(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    NAME=models.CharField("NAME",max_length=50)
    STUSPS=models.CharField("STUSPS",max_length=50)

    #area = models.IntegerField()
    #pop2005 = models.IntegerField("Population 2005")
    #fips = models.CharField("FIPS Code", max_length=2, null=True)
    #iso2 = models.CharField("2 Digit ISO", max_length=2)
    #iso3 = models.CharField("3 Digit ISO", max_length=3)
    #un = models.IntegerField("United Nations Code")
    #region = models.IntegerField("Region Code")
    #subregion = models.IntegerField("Sub-Region Code")
    #lon = models.FloatField()
    #lat = models.FloatField()

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    mpoly = models.MultiPolygonField()#"MULTIPOLYGON")

    # Returns the string representation of the model.
    def __str__(self):
        return self.NAME