from django.db import models
from . import OrderInfo


class BillingAddress(models.Model):
    order = models.ForeignKey(OrderInfo, on_delete=models.PROTECT)
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    email = models.CharField(verbose_name="email", max_length=60)
    phone = models.CharField(max_length=15, blank=True)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, blank=True)
    postal_code = models.CharField(max_length=15, blank=True)
    city = models.CharField(max_length=100)
    user_id = models.CharField(max_length=15, blank=True)

    class Meta:
        db_table = 'BillingAddress'