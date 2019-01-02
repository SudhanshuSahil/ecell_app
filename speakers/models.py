from django.db import models
from common.v1.utils.helpers import get_url_friendly
from common.models import LifeTimeTrackingModel, ActiveModel

# Create your models here.
class Speaker(ActiveModel):
    name = models.CharField(max_length=200, blank=True, null=True, default=None)
    limkedin_link = models.URLField(blank=True, null=True, default=None)
    photo_url = models.URLField(blank=True, null=True, default=None)
    company = models.CharField(max_length=200,blank=True, null=True, default=None)
    designation = models.CharField(max_length=200,blank=True, null=True, default=None)

    class Meta:
        verbose_name = "Speaker"
        verbose_name_plural = "Speaker"
        ordering = ("-created_at",)

