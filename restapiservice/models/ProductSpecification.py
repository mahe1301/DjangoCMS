from django.db import models
from . import Product,SpecificationCategory


class ProductSpecification(models.Model):
    name = models.TextField(blank=False,null=False)
    detail = models.TextField(blank=False,null=False)
    category = models.ForeignKey(SpecificationCategory, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    created = models.DateTimeField(db_column="created date",auto_now_add=True, blank=True)
    modified = models.DateTimeField(db_column="modified date", auto_now=True)
    isActive = models.BooleanField(default=False)

    class Meta:
        db_table = 'ProductSpecification'