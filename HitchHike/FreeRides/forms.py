from django import forms
from django.contrib.gis.db import models
from leaflet.forms import fields
from .models import Rides
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User


class rideForm(forms.ModelForm):

    class Meta:
        model = Rides
        fields = ('user', 'location', 'destination', 'location_name', 'destination_name', 'ride_date', 'price', 'phone', 'description', 'seats')

    def save(self, commit=True):
        ride = super(rideForm, self).save(commit=False)
        if commit:
            ride.save()
        return ride


class EditProfileForm(UserChangeForm):
    template_name='/something/else'

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            
        )
