from django.db import models
from common.v1.utils.helpers import get_url_friendly
from common.models import LifeTimeTrackingModel, ActiveModel

# Create your models here.
class Sponsor(ActiveModel):
    name = models.CharField(max_length=200, blank=True, null=True, default=None)
    link = models.URLField(blank=True, null=True, default=None)
    photo = models.URLField(blank=True, null=True, default=None)
    category = models.CharField(max_length=200,blank=True, null=True, default=None)

    class Meta:
        verbose_name = "Sponsor"
        verbose_name_plural = "Sponsors"
        ordering = ("-created_at",)
