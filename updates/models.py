from django.db import models
from common.models import LifeTimeTrackingModel, ActiveModel

class Update(ActiveModel):
    # id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    # update_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default=None)
    description = models.TextField(blank=True)
