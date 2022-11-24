from django.db import models


class RideModel(models.Model):
    ride_id = models.CharField(max_length=200, blank=True, null=True)
    rideable_type = models.CharField(max_length=200,blank=True, null=True)
    started_at = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    ended_at = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    start_station_name = models.CharField(max_length=200, blank=True, null=True)
    start_station_id = models.CharField(max_length=200, blank=True, null=True)
    end_station_name = models.CharField(max_length=200, blank=True, null=True)
    end_station_id = models.CharField(max_length=200, blank=True, null=True)
    start_lat = models.DecimalField(max_digits=6, decimal_places=4, default=0.0, blank=True, null=True)
    start_lng = models.DecimalField(max_digits=6, decimal_places=4, default=0.0, blank=True, null=True)
    end_lat = models.DecimalField(max_digits=6, decimal_places=4, default=0.0, blank=True, null=True)
    end_lng = models.DecimalField(max_digits=6, decimal_places=4, default=0.0, blank=True, null=True)

    def __str__(self):
        return self.ride_id



