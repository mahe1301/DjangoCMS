from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from ..models import TrackingInfo,OrderItemInfo,OrderInfo
from restapiservice.serializers.ordertrackingserializer import OrderTrackingSerializer
from restapiservice.serializers.orderitemserializer import OrderItemSerializer
from ..permissions.userpermissions import IsBasicUser



@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def user_orders(request):

    order_id_list = OrderInfo.objects.filter(user=request.data['userid'])
    order_track = TrackingInfo.objects.filter(order_id__in=list(order_id_list))
    serializer = OrderTrackingSerializer(order_track, many=True)
    return Response(serializer.data)



@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def user_order_items(request):
    try:
        order_items = OrderItemInfo.objects.filter(order_id=request.data['orderid'])
        serializer = OrderItemSerializer(order_items, many=True,context={"request": request})
    except Exception as e:
        serializer.data = str(e)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsBasicUser, ])
def track_status(request):
    order_track = TrackingInfo.objects.filter(tracking_reference=request.data['trackingid'])
    data={'status': str(order_track[0].status)}
    return Response(data)