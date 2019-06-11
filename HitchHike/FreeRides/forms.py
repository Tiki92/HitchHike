from django import forms
from django.contrib.gis.db import models
from leaflet.forms import fields
from .models import Rides
#from django.contrib.gis import forms


class rideForm(forms.ModelForm):
    #user = forms.CharField(required=False)
    #location_name = forms.CharField(required=False)
    #location =  forms.PointField(required=False)
    #destination_name = forms.CharField(required=False)
    #destination = forms.PointField(required=False)
    #ride_date = forms.DateTimeField()


    class Meta:
        model = Rides
        fields = ('user', 'location', 'destination', 'location_name', 'destination_name', 'ride_date', 'price', 'phone', 'description')

    def save(self, commit=True):
        ride = super(rideForm, self).save(commit=False)
        #ride.user = self.cleaned_data['user']
        #ride.location_name = self.cleaned_data['location_name']
        #ride.location = self.cleaned_data['location']
        #ride.destination_name = self.cleaned_data['destination_name']
        #ride.destination = self.cleaned_data['destination']
        if commit:
            ride.save()
        return ride
