from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from ..models import TrackingInfo,OrderItemInfo,OrderInfo
from restapiservice.serializers.socialauthserializer import GoogleSocialAuthSerializer
from rest_framework import  status
from ..permissions.userpermissions import IsBasicUser

@api_view(['POST'])
@permission_classes([IsBasicUser, ])
def Verify_google_user(request):
    serializer = GoogleSocialAuthSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    data = ((serializer.validated_data)['auth_token'])
    return Response(data, status=status.HTTP_200_OK)