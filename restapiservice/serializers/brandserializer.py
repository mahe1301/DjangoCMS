from rest_framework import serializers
from ..models import Brands

class BrandSerializer(serializers.ModelSerializer):


    class Meta:
        model=Brands
        fields=['id','name','vendorInfo','isActive']

