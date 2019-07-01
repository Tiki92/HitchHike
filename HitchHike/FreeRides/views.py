from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Rides
from django.core.serializers import serialize
import json
from .forms import rideForm, EditProfileForm
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.gis.geoip2 import GeoIP2
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def index(request):
    loc = serialize('geojson', Rides.objects.all())
    dec_loc = json.loads(loc)

    obj = Rides.objects.all()
    paginator = Paginator(obj, 12)
    

    query = request.GET.get('q', None)
    if query is not None:
        rides = obj.filter(
            Q(location_name__icontains=query))
        paginator = Paginator(rides, 12)
        
    page = request.GET.get('page')
    rides = paginator.get_page(page)

    g = GeoIP2()
    ip = "185.86.151.11"
    user_loc_lat = g.lat_lon(ip)[0]
    user_loc_lon = g.lat_lon(ip)[1]
    
    context = {'dec_loc':loc, 'rides': rides, 'user_loc_lat': user_loc_lat, 'user_loc_lon': user_loc_lon, 'obj': obj}
    return render(request, 'Home.html', context)

@login_required
def profile_view(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = User.objects.get(username=request.user)
    args = {'user':user}
    return render(request, 'account/Profile.html', args)

@login_required
def add_ride(request):
    if request.method == "POST":
        form =rideForm(request.POST)
        if form.is_valid():
            form.cleaned_data
            post = form.save(commit=False)
            form.save()
            return HttpResponse("FUCKK!!YOUUU!!")

        return HttpResponse(form.errors)

    return render(request, 'add_ride.html')


def detailed(request,ride_id):
    details = Rides.objects.all()
    ride = Rides.objects.get(id=ride_id)
    context = {'details': details, 'ride': ride}
    return render(request, "detailed.html", context)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/accounts/profile/')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'account/edit_profile.html', args)
