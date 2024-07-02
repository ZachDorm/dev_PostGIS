from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from geo_init.forms import MyGeoForm


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

    return render(request, "name.html", {"form": form})



from django.views.generic import DetailView
from .models import States


class StatesTrial(DetailView):
    """
        City detail view.
    """
    template_name = 'map1/name.html'
    model = States

    
def test(request):
 
    return HttpResponse(States.objects.all().values())



    
def get_all(request):
    dat = States.objects.all().values()
    context = {
        'state' : dat
    }
    return render(context, request)