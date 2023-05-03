from rest_framework import serializers

from ..models import WishList
from .productserializer import *


class WishListSerializer(serializers.ModelSerializer):

    class Meta:
        model=WishList
        fields=['id', 'user', 'Product']  # 'created', 'modified', 'isActive'


class WishListInfoSerializer(serializers.ModelSerializer):
    Product=ProductSerializer()
    class Meta:
        model=WishList
        fields=['id', 'user', 'Product']  # 'created', 'modified', 'isActive'


