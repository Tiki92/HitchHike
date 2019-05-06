from django.shortcuts import render
from .models import Rides
from django.core.serializers import serialize
import json
from .forms import rideForm
from django.http import HttpResponse

# Create your views here.
def index(request):
    loc = serialize('geojson', Rides.objects.all())
    dec_loc = json.loads(loc)

    context = {'dec_loc':dec_loc}
    return render(request, 'Home.html', context)

def profile_view(request):
    user = request.user
    args = {'user':user}
    return render(request, 'Home.html', args)

def add_ride(request):
    user = request.user
    args = {'user':user}

    if request.method == 'POST':
        response_data = request.POST.get('location')
        response_data['message'] = "FUCK!!"
        return HttpResponse(response_data, content_type="application/json")

    return render(request, 'add_ride.html', args)

def yes(request):
    if request.method == "POST":
        form =rideForm(request.POST)
        if form.is_valid():
            form.cleaned_data
            post = form.save(commit=False)
            #post.user = request.user
            #post.location = request.POST.get("location")
            #post.location_name = request.POST.get("location_name")
            #post.destination = request.POST.get("destination")
            #post.destination_name = request.POST.get("destination_name")

            form.save()
            return HttpResponse("FUCKK!!YOUUU!!")

        return HttpResponse(form.errors)
        #request.POST.get("location")
