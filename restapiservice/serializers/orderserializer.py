from rest_framework import serializers
from ..models import OrderInfo


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderInfo
        fields=['id','payment_status','payment_amount','coupon_code','coupon_amount','userType','user','bank_reference','created','payment_method','shipping_amount']
