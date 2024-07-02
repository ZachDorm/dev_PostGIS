from django.contrib.gis import forms
from . import models
from django.forms import ModelForm
from geo_test2.models import States
from django.contrib.gis.forms.widgets import OSMWidget

class MyGeoForm(forms.Form):
    point = forms.TextInput(attrs={'class': 'form-input'})#forms.PolygonField(widget=forms.OSMWidget(attrs={"template_name":"gis/openlayers-osm.html","default_lat": 0,"default_lon": 0}))

    #"display_raw": True


class GeoForm(ModelForm):
    #formtest = forms.PointField(widget=forms.OSMWidget(attrs={"template_name": "gis/openlayers.html"}))#forms.MultiPolygonField(widget=forms.OSMWidget(attrs={'map_width': 800, 'map_height': 500}))

    class Meta:
         model = States
         fields = ["NAME", "STUSPS", "mpoly"]
         wid = OSMWidget(attrs={'default_lat':36, 'default_lon':-84, 'default_zoom':8, 'label':'Map'})
         widgets = {
            'NAME': forms.TextInput(attrs={'class': 'form-input', 'label':'State name'}),
            'STUSPS': forms.TextInput(attrs={'class': 'form-input', 'label':'USPS State Code'}),
            'mpoly': wid}#forms.OSMWidget}
