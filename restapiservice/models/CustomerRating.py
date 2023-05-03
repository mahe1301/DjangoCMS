from django.db import models
from . import UserInfo,Product, OrderInfo
from django.core.validators import MaxValueValidator, MinValueValidator


class CustomerRating(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.PROTECT)
    Product = models.ForeignKey(Product, on_delete=models.PROTECT)
    created = models.DateTimeField(db_column="created date",auto_now_add=True, blank=True)
    modified = models.DateTimeField(db_column="modified date", auto_now=True)
    rating = models.IntegerField(default=1,validators=[MaxValueValidator(5), MinValueValidator(1)])
    description = models.TextField(blank=True)
    order = models.ForeignKey(OrderInfo, on_delete=models.PROTECT)

    class Meta:
        db_table = 'CustomerRating'

