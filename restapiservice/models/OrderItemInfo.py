from django.db import models
from . import OrderInfo,Product


class OrderItemInfo(models.Model):
    order = models.ForeignKey(OrderInfo, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    created = models.DateTimeField(db_column="created date",auto_now_add=True, blank=True)
    actual_amount = models.IntegerField()
    discount_amount = models.IntegerField()
    product_bill_amount = models.IntegerField()
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'OrderItemInfo'
