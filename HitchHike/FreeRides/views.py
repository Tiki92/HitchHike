from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Rides
from django.core.serializers import serialize
import json
from .forms import rideForm
from django.http import HttpResponse
from django.db.models import Q

# Create your views here.
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1]
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
    
    context = {'dec_loc':loc, 'rides': rides}
    return render(request, 'Home.html', context)

def profile_view(request):
    user = request.user
    args = {'user':user}
    return render(request, 'account/Profile.html', args)

def add_ride(request):
    user = request.user
    args = {'user':user, 'form':rideForm}

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

        return HttpResponse(form['ride_date'].errors)
