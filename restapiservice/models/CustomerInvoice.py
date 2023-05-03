from django.db import models
from . import OrderInfo,Product

class CustomerInvoice(models.Model):
    order = models.ForeignKey(OrderInfo, on_delete=models.PROTECT)
    created = models.DateTimeField(db_column="created date",auto_now_add=True, blank=True)
    modified = models.DateTimeField(db_column="modified date", auto_now=True)
    amount = models.IntegerField(blank=False,null=False)
    description = models.CharField(max_length=255)

    class Meta:
        db_table = 'CustomerInvoice'