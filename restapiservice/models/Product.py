from django.db import models
from . import ProductCategory,Brands
from  ..utils import image

class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT)
    brands = models.ForeignKey(Brands, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    imageUrl = models.CharField(max_length=255, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    discountprice = models.IntegerField(blank=True, null=True)
    inCart = models.BooleanField(default=False)
    numbersInCart = models.IntegerField(default=0)
    quantity = models.IntegerField(blank=True, null=True)
    isActive = models.BooleanField(default=True)
    isTopSeller = models.BooleanField(default=True)
    isComboProduct = models.BooleanField(default=True)
    img = models.ImageField(upload_to=image.upload_product,blank=True, null=True)
    averageRating=models.DecimalField(blank=True, null=True,max_digits=5, decimal_places=2)
    gstPercent=models.DecimalField(default=0,max_digits=2, decimal_places=2)   
    class Meta:
        db_table = 'Product'
        ordering = ['-id']

