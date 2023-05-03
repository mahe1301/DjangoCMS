from django.db import models
from . import Product
from  ..utils import image
# Create your models here.


class ProductImages(models.Model):
    # id= models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    description = models.CharField(max_length=255, blank=True, null=True)
    ImageUrl = models.ImageField(upload_to=image.upload_product_images, blank=True, null=True) # overwrite=True
    isActive = models.BooleanField(default=True)

    class Meta:
        db_table = 'ProductImages'
