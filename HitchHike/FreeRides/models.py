from __future__ import unicode_literals
from django.contrib.gis.db import models

# Create your models here.

class Rides(models.Model):
    user = models.CharField(max_length=30, default='admin')
    location_name = models.CharField(max_length=300)
    location = models.PointField(srid=4326)
    destination_name = models.CharField(max_length=300)
    destination = models.PointField(srid=4326)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = " Rides"
