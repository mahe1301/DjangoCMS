from django.db import models


class CouponInfo(models.Model):
    coupon_code = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(db_column="created date",auto_now_add=True, blank=True)
    modified = models.DateTimeField(db_column="modified date", auto_now=True)
    start_date = models.DateField(verbose_name="start date", blank=True)
    end_date = models.DateField(verbose_name="end date", blank=True)
    disc_percent = models.FloatField(blank=True)
    disc_min_order_amount = models.IntegerField(blank=True)
    disc_max_limit = models.IntegerField(blank=True)
    isActive = models.BooleanField(default=False)

    class Meta:
        db_table = 'CouponInfo'