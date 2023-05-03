from rest_framework import serializers
from ..models import Product,ProductImages
from .brandserializer import *
from .productcategoryserializer import *
from .productimageserializer import *


class ProductSerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer()
    brands = BrandSerializer()
    productimages = serializers.SerializerMethodField('get_product_images')

    def get_product_images(self, value):
        img_obj = ProductImages.objects.filter(product_id=value.id).values_list('ImageUrl',flat=True)
        return img_obj

    class Meta:
        model=Product
        fields=['productimages','category','brands','id','name','description','imageUrl','price','discountprice','quantity','inCart','numbersInCart','isActive','img','isTopSeller','isComboProduct','averageRating']
         
