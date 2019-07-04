from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.core.serializers import serialize
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.gis.geoip2 import GeoIP2
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import rideForm, EditProfileForm
from .models import Rides
import json

class homeView(TemplateView):
    template_name = 'Home.html'

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def get(self, request):
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
        ip = "185.86.151.11" # self.get_client_ip(request)
        user_loc_lat = g.lat_lon(ip)[0]
        user_loc_lon = g.lat_lon(ip)[1]
        
        context = {'dec_loc':loc, 'rides': rides, 'user_loc_lat': user_loc_lat,
         'user_loc_lon': user_loc_lon, 'obj': obj}
        return render(request, 'Home.html', context)

class profile(TemplateView):
    template_name = 'account/Profile.html'
    user = ''
  
    def get(self, request, pk=None):
        user = 0
        if pk:
            user = User.objects.get(pk=pk)
        else:
            user = User.objects.get(username=request.user)
        args = {'user':user}
        return render(request, 'account/Profile.html', args)


class addRide(TemplateView):
    template_name = 'add_ride.html'

    def post(self, request):
        form =rideForm(request.POST)
        if form.is_valid():
            form.cleaned_data
            post = form.save(commit=False)
            form.save()
            return HttpResponse("Nice!!")



class detailed(TemplateView):
    template_name = "detailed.html"


class editProfile(TemplateView):
    template_name = 'account/edit_profile.html'