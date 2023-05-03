from rest_framework import serializers
from restapiservice.serializers.userinfoserializer import UserInfoSerializer

from ..models import CustomerRating


class CustomerRatingSerializer(serializers.ModelSerializer):
    user=UserInfoSerializer()
    
    class Meta:
        model = CustomerRating
        fields = ['id', 'user', 'Product', 'rating', 'description','order']
        extra_kwargs = {'rating': {'required': True, 'min_value': 1, 'max_value': 5},
                        'id': {'read_only': True},
                        'description': {'required': True}}


class CustomerRatingPostSerializer(serializers.ModelSerializer):


    class Meta:
        model = CustomerRating
        fields = ['id', 'user', 'Product', 'rating', 'description','order']
        extra_kwargs = {'rating': {'required': True, 'min_value': 1, 'max_value': 5},
                        'id': {'read_only': True},
                        'description': {'required': True}}