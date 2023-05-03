from django.db import models
from . import UserInfo,UserContact


class OrderInfo(models.Model):
    created = models.DateTimeField(db_column="created date",auto_now_add=True, blank=True)
    modified = models.DateTimeField(db_column="modified date", auto_now=True)
    payment_status = models.TextField(blank=False,null=False)
    payment_amount = models.IntegerField()
    coupon_code = models.CharField(max_length=30,blank=False,null=False)
    coupon_amount = models.IntegerField(blank=True, null=True)
    userType = models.CharField(max_length=30,blank=True, null=True)
    user = models.TextField(blank=True, null=True)
    bank_reference = models.TextField(blank=True, null=True)
    payment_method = models.CharField(max_length=30,blank=True,null=True)
    shipping_amount = models.IntegerField(blank=True,null=True)
    class Meta:
        db_table = 'OrderInfo'

