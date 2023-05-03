from django.db import models
from . import OrderInfo


class TrackingInfo(models.Model):
    tracking_reference = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=255)
    Comments = models.CharField(max_length=255)
    order = models.ForeignKey(OrderInfo, on_delete=models.PROTECT)

    class Meta:
        db_table = 'TrackingInfo'