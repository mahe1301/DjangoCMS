from rest_framework import serializers
from ..models import OrderItemInfo,CustomerRating
from .orderserializer import *
from .productserializer import *
from.customerratingserializer import *
from django.db.models import Q


# class OrderItemSerializer(serializers.ModelSerializer):
#     order = OrderSerializer()
#     product = ProductSerializer()
#     rating = serializers.SerializerMethodField('get_customer_ratings')

#     def get_customer_ratings(self, value):
#         rating_obj = CustomerRating.objects.filter(Q(order_id=value.order_id) & Q(Product_id=value.product_id) )
#         serializer = CustomerRatingSerializer(rating_obj, many=True)
#         return serializer.data

#     class Meta:
#         model=OrderItemInfo
#         fields=['order','product','quantity','actual_amount','discount_amount','product_bill_amount','description','rating']

from rest_framework import serializers
from ..models import OrderItemInfo,CustomerRating,TrackingInfo
from .orderserializer import *
from .productserializer import *
from.customerratingserializer import *
from django.db.models import Q


class OrderItemSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    product = ProductSerializer()
    rating = serializers.SerializerMethodField('get_customer_ratings')
    trackstatus = serializers.SerializerMethodField('get_track_status')

    def get_customer_ratings(self, value):
        rating_obj = CustomerRating.objects.filter(Q(order_id=value.order_id) & Q(Product_id=value.product_id) )
        serializer = CustomerRatingSerializer(rating_obj, many=True)
        return serializer.data
    
    def get_track_status(self, value):
        actual_status="invalid"
        try:
            track_obj = TrackingInfo.objects.get(Q(order_id=value.order_id))
            actual_status=track_obj.status
        except Exception as e:
            pass
        return actual_status

    class Meta:
        model=OrderItemInfo
        fields=['order','product','quantity','actual_amount','discount_amount','product_bill_amount','description','rating','trackstatus']