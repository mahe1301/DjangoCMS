from rest_framework import serializers
from ..models import ProductImages



class ProductImageSerializer(serializers.ModelSerializer):


    class Meta:
        model=ProductImages
        fields=['description','ImageUrl','isActive']