from django.db import models
from . import OrderInfo


class OrderCancellationRequest(models.Model):
    order = models.ForeignKey(OrderInfo, on_delete=models.PROTECT)
    created = models.DateTimeField(db_column="created date",auto_now_add=True, blank=True)
    modified = models.DateTimeField(db_column="modified date", auto_now=True)
    refund_id = models.TextField(blank=True,null=True)
    refund_status = models.TextField(blank=True,null=True)
    comment = models.CharField(max_length=255)
    request_status =models.CharField(max_length=255,blank=False,null=False)
    request_time_track_status =models.CharField(max_length=255,blank=False,null=False,default='Pending')
    isActive = models.BooleanField(default=True)
    class Meta:
        db_table = 'OrderCancellationRequest'