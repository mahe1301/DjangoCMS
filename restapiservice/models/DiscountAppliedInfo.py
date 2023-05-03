from django.db import models
from . import OrderInfo


class DiscountAppliedInfo(models.Model):
    order = models.ForeignKey(OrderInfo, on_delete=models.PROTECT)
    created = models.DateTimeField(db_column="created date",auto_now_add=True, blank=True)
    modified = models.DateTimeField(db_column="modified date", auto_now=True)
    disc_amount = models.FloatField()
    description = models.CharField(max_length=255)

    class Meta:
        db_table = 'DiscountAppliedInfo'
