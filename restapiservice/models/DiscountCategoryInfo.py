from django.db import models
from . import Product


class DiscountCategoryInfo(models.Model):
    Category_Types = (
        ('P', 'ProductWise'),
        ('A', 'AmountWise'),
        ('C', 'CouponWise'),
        ('U', 'UserWise')
    )
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=1, choices=Category_Types)
    created = models.DateTimeField(db_column="created date",auto_now_add=True, blank=True)
    modified = models.DateTimeField(db_column="modified date", auto_now=True)
    disc_percent = models.FloatField(blank=True)
    disc_limit = models.IntegerField(blank=True)
    isActive = models.BooleanField(default=False)

    class Meta:
        db_table = 'DiscountCategoryInfo'
