from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template import loader
from geo_init.forms import MyGeoForm, GeoForm
from . import views
from .models import States
import folium


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = GeoForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = GeoForm()

    return render(request, "geo_init/name.html", {"form": form})


def thanks(request):
    return render(request, "geo_init/thanks.html")

def nav(request):
    return render(request, "geo_init/nav_temp.html")

    
#returns all features in the database using get.html
def get_all(request):
    dat = States.objects.all().values()

    template = loader.get_template('geo_init/get.html')
    context = {
        'dat' : dat,
    }
    return HttpResponse(template.render(context, request))

    
def test(request):
    return HttpResponse(States)

    #return HttpResponse(States.objects.get(NAME="Tennessee").mpoly.wkt)

def show_map(request):
    m = folium.Map([10,10], zoom_start=10)

    states_list = States.objects.values_list("NAME", flat=True)
    for i in states_list:
        folium.GeoJson(data=States.objects.get(NAME=i).mpoly.geojson).add_to(m)
        m.fit_bounds(m.get_bounds())
    m = m._repr_html_()
    context = {'map':m,}

    return render(request, 'geo_init/thanks.html', context)


def home(request):
    if 'test' in request.POST:
        return render(request, 'geo_init/thanks.html', context)