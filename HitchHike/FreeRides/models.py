from __future__ import unicode_literals
from django.contrib.gis.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Rides(models.Model):
    user = models.CharField(max_length=30, default='admin')
    location_name = models.CharField(max_length=300)
    location = models.PointField(srid=4326)
    destination_name = models.CharField(max_length=300)
    destination = models.PointField(srid=4326)
    ride_date = models.DateTimeField(blank=True)
    price = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2, default=0)
    phone = models.CharField(max_length=20, null=False, blank=False, unique=False)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = " Rides"
