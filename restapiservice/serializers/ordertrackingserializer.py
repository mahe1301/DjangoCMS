from rest_framework import serializers
from ..models import TrackingInfo
from .orderserializer import *


class OrderTrackingSerializer(serializers.ModelSerializer):
    order = OrderSerializer()

    class Meta:
        model = TrackingInfo
        fields=['id','tracking_reference','status','Comments','order']