from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from ..models import CustomerRating
from restapiservice.serializers import CustomerRatingSerializer,CustomerRatingPostSerializer
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from ..utils.averagerating import calc_average_rating
from ..permissions.userpermissions import IsBasicUser


@api_view(['POST'])
@permission_classes([IsBasicUser, ])
def customer_rating_list(request):
    customer_rating_obj=CustomerRating.objects.filter(Product_id=request.data['productid'])
    if len(customer_rating_obj) != 0:
        serializer = CustomerRatingSerializer(customer_rating_obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def customer_rating_update(request):
    serializer = CustomerRatingPostSerializer(data=request.data)
    if serializer.is_valid():
        customer_rating_obj = CustomerRating.objects.filter(
            Q(user_id=request.data['user']) & Q(Product_id=request.data['Product']) & Q(order_id=request.data['order']))
        if len(customer_rating_obj) == 0:
            serializer.save()
        else:
            customer_rating_obj[0].rating = int(request.data['rating'])
            customer_rating_obj[0].description = request.data['description']
            customer_rating_obj[0].save()
        calc_average_rating(request.data['Product'])
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
