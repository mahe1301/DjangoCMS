from django.db import models
from . import TrackingInfo,OrderInfo,CustomerInvoice


class PaymentInfo(models.Model):
    invoice = models.ForeignKey(CustomerInvoice, on_delete=models.PROTECT)
    Order = models.ForeignKey(OrderInfo, on_delete=models.PROTECT)
    tracking = models.ForeignKey(TrackingInfo, on_delete=models.PROTECT,blank=True,null=True)
    paymentStatus = models.CharField(max_length=255)
    created = models.DateTimeField(db_column="created date", auto_now_add=True, blank=True)
    modified = models.DateTimeField(db_column="modified date", auto_now=True)

    class Meta:
        db_table = 'PaymentInfo'