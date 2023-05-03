from django.db import models
from . import UserInfo, Product, OrderInfo
from django.core.validators import MaxValueValidator, MinValueValidator


class CustomerSubscribe(models.Model):
    email = models.CharField(verbose_name="email",max_length=60,unique=True)
    created = models.DateTimeField(auto_now_add=True,blank=True)
    modified = models.DateTimeField(db_column="modified date", auto_now=True)
    isActive = models.BooleanField(default=True)

    class Meta:
        db_table = 'CustomerSubscribe'