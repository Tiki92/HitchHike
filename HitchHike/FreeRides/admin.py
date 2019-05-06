from django.contrib import admin
from .models import Rides
from leaflet.admin import LeafletGeoAdmin

 #Register your models here.

class RidesAdmin(LeafletGeoAdmin):

    list_display = ('location_name', 'destination_name', 'user')


admin.site.register(Rides, RidesAdmin)
