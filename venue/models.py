"""Models for Locations."""
from uuid import uuid4
from django.db import models
from common.models import LifeTimeTrackingModel, ActiveModel

class Venue(ActiveModel):
    """A unique location, chiefly venues for events.

    Attributes:
        `lat` - Latitude
        'lng` - Longitude
    """

    # id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    venue_id = models.AutoField(primary_key=True)
    # time_of_creation = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    lat = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    lng = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    # reusable = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Venue"
        verbose_name_plural = "Venue"
        ordering = ("name",)
