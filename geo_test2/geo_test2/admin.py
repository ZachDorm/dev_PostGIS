from django.contrib.gis import admin
from .models import States
from geo_init.forms import GeoForm

admin.site.register(States, admin.GISModelAdmin)

#admin.site.register(MyGeoForm)