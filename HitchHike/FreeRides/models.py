from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models
from decimal import Decimal


class Rides(models.Model):
    location_name = models.CharField(max_length=20)
    location = models.PointField(srid=4326)
    destination_name = models.CharField(max_length=20)
    destination = models.PointField(srid=4326)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural =  " Rides"
