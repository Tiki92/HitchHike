from django.shortcuts import render
from .models import Rides
from django.core.serializers import serialize
import json
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
    loc = serialize('geojson', Rides.objects.all())
    dec_loc = json.loads(loc)
    #lat = dec_loc['features'][0]['geometry']['coordinates'][0]
    #long = dec_loc['features'][0]['geometry']['coordinates'][1]
    #"lat":lat, 'long':long, 'response': response,'loc': loc,'locations': locations
    #response = JsonResponse(loc, safe=False)
    #locations = serialize('geojson', Rides.objects.all())
    context = {'dec_loc': dec_loc}
    return render(request, 'Home.html', context)

def profile_veiew(request):
    user = request.user
    args = {'user': user,}
    return render(request, 'account/Profile.html', args)

def add_ride(request):

    return render(request, 'add_ride.html')

def loc_data(request):
    locations = serialize('geojson', Rides.objects.all())
    return HttpResponse(locations, content_type='json')
