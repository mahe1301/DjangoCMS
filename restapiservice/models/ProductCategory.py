from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=255,unique=True)
    parentCategory = models.IntegerField(blank=True,null=True)
    isActive = models.BooleanField(default=True)

    class Meta:
        db_table = 'ProductCategory'

