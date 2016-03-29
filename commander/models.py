from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Shot(models.Model):
    registered_date = models.DateTimeField(default=timezone.now)
    IOT_id = models.CharField(max_length=20, default='-1')
    gps_lat = models.CharField(max_length=20)
    gps_long = models.CharField(max_length=20)
    gps_elev = models.CharField(max_length=20)
    heading_point = models.CharField(max_length=20)

    def publish(self):
        self.registered_date = timezone.now()
        self.save()

    def __str__(self):

        return self.IOT_id.__str__() + '@' + self.registered_date.__str__()

# Create your models here.
