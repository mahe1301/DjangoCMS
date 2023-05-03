from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from ..models import OrderInfo
from rest_framework.response import Response
from rest_framework import status
from ..utils.ordercancel import proceed_cancellation_request
from ..utils.customlogger import customlogger

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def order_cancel(request):
    try:
        cust=customlogger()
        resp={'detail': "invalid",'code':'not_cancel'}
        if 'orderid' in request.data.keys() and 'comment' in request.data.keys():
            order_cancel_status = proceed_cancellation_request(request.data['orderid'],request.data['comment'])
            if order_cancel_status == 1:
                resp={'detail': "cancelled Successfully ",'code':'cancel_done'}
            else:
                resp={'detail': "Not cancelled Successfully",'code':'not_cancel'}   
    except Exception as e:
        cust.loggerInfo.error(str(e))
    finally:
        return Response(resp, status=status.HTTP_200_OK)