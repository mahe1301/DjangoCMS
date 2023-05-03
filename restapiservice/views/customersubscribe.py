from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from ..models import CustomerSubscribe
from rest_framework.response import Response
from rest_framework import status
from ..utils.customlogger import customlogger
from ..permissions.userpermissions import IsBasicUser 

@api_view(['POST'])
@permission_classes([IsBasicUser, ])
def customer_subscribe(request):
    try:
        cust=customlogger()
        resp={'detail': "invalid",'code':'not_valid'}
        if 'emailid' in request.data.keys():
        
            customer_subscribe_obj=CustomerSubscribe.objects.filter(email=request.data['emailid'])
            if len(customer_subscribe_obj) == 0 :
                customer_subscribe_obj=CustomerSubscribe()
                customer_subscribe_obj.email=request.data['emailid']
                customer_subscribe_obj.save()
                resp={'detail': "Added Successfully ",'code':'success'}
            else:
                if customer_subscribe_obj.isActive == False:
                    customer_subscribe_obj.isActive=True
                    customer_subscribe_obj.save()
                    resp={'detail': "Updated Successfully ",'code':'success'}
                else:
                    resp={'detail': "Already exists ",'code':'duplicate'}
 
    except Exception as e:
        cust.loggerInfo.error(str(e))
    finally:
        return Response(resp, status=status.HTTP_200_OK)
    