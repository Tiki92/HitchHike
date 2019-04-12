from django.contrib import admin
from .models import Rides
from leaflet.admin import LeafletGeoAdmin

 #Register your models here.

class RidesAdmin(LeafletGeoAdmin):
    pass
    #list_display = ('location_name', 'location', 'destination_name', 'destination')


admin.site.register(Rides, RidesAdmin)
