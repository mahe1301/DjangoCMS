from django.db import models
from . import UserInfo,Product
from django.core.validators import MaxValueValidator, MinValueValidator


class WishList(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.PROTECT)
    Product = models.ForeignKey(Product, on_delete=models.PROTECT)
    created = models.DateTimeField(db_column="created date",auto_now_add=True, blank=True)
    modified = models.DateTimeField(db_column="modified date", auto_now=True)
    isActive = models.BooleanField(default=True)

    class Meta:
        db_table = 'WishList'
