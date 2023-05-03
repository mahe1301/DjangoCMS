from django.db import models


class Brands(models.Model):
    name = models.CharField(max_length=255,unique=True)
    vendorInfo = models.CharField(max_length=255,blank=True,null=True)
    isActive = models.BooleanField(default=True)

    class Meta:
        db_table = 'Brands'
