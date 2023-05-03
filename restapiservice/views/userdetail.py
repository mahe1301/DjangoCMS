from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from ..models import UserInfo,UserContact
from restapiservice.serializers.usercontactserializer import UserContactSerializer
from restapiservice.serializers.userinfoserializer import UserInfoSerializer
from rest_framework.response import Response
from rest_framework import  status


@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def user_info_update(request):
    serializer = UserInfoSerializer(data=request.data)
    if serializer.is_valid():
        # serializer.save()
        user_obj=UserInfo.objects.get(id=request.data['id'])
        user_obj.first_name = request.data['first_name']
        user_obj.last_name = request.data['last_name']
        user_obj.phone = request.data['phone']
        user_obj.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def user_contact_update(request):
    serializer = UserContactSerializer(data=request.data)
    if serializer.is_valid():
        # serializer.save()
        #  user_contact_obj = UserContact.objects.filter(user_id=request.data['user']).first()
         user_contact_obj = UserContact.objects.filter(user_id=request.data['user'])
         #print(len(user_contact_obj))
         if len(user_contact_obj) == 0:
             user_contact_obj = UserContact()
             user_contact_obj.user_id = request.data['user']
         else:
             user_contact_obj = user_contact_obj[0]
         user_contact_obj.user_id=request.data['user']
         user_contact_obj.address1 = request.data['address1']
         user_contact_obj.address2 = request.data['address2']
         user_contact_obj.postalcode = request.data['postalcode']
         user_contact_obj.city = request.data['city']
         user_contact_obj.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
