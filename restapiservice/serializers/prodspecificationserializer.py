from rest_framework import serializers
from ..models import ProductSpecification


class ProductSpecificationSerializer(serializers.ModelSerializer):


    class Meta:
        model=ProductSpecification
        fields=['name','detail','category','product','isActive']