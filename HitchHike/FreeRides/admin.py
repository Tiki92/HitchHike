from django.contrib import admin
from .models import Rides, localUsers
from leaflet.admin import LeafletGeoAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

 #Register your models here.


class RidesAdmin(LeafletGeoAdmin):

    list_display = ('location_name', 'destination_name', 'user')

class localUsersInline(admin.StackedInline):
    model = localUsers
    can_delete = False
    verbose_name_plural = 'localUsers'

class UserAdmin(BaseUserAdmin):
    inlines = (localUsersInline,)

admin.site.register(Rides, RidesAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
