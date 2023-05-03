from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from ..models import CouponInfo
from django.db.models import Q
from ..utils.customlogger import customlogger
from ..permissions.userpermissions import IsBasicUser

@api_view(['POST'])
@permission_classes([IsBasicUser, ])
def coupon_check(request):
    try:
        cust=customlogger()
        resp = {
            'discountAmount': 0,
            'couponApplied' : False
        }
        if 'couponcode' in request.data.keys():
            coupon_obj = CouponInfo.objects.get( Q(coupon_code=request.data['couponcode']) & Q(isActive=1))
            purchase_amount=int(request.data['totalamount'])
            if purchase_amount > 0:
                if purchase_amount >= coupon_obj.disc_min_order_amount:
                    disc_amt = (purchase_amount * coupon_obj.disc_percent) / 100
                    if disc_amt > coupon_obj.disc_max_limit:
                        disc_amt =  coupon_obj.disc_max_limit 
                    resp['discountAmount'] =disc_amt
                    resp['couponApplied'] = True
        else:
            raise Exception("No couponcode parameter ")
    except Exception as e:
        cust.loggerInfo.error(str(e))
    return Response(resp)