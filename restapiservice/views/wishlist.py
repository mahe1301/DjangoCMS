from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from ..models import WishList,Product
from restapiservice.serializers import WishListSerializer,ProductSerializer,WishListInfoSerializer
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q


@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def wish_list_update(request):
    serializer = WishListSerializer(data=request.data)
    if serializer.is_valid():
        wish_list_obj=WishList.objects.filter( Q(user_id=request.data['user']) & Q(Product_id=request.data['Product']) & Q(isActive=1))
        if len(wish_list_obj) == 0:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def wish_list_retrieve(request):
    wish_list_obj=WishList.objects.filter( Q(user_id=request.data['userid']) & Q(isActive=1))
    if len(wish_list_obj) != 0:
        serializer = WishListInfoSerializer(wish_list_obj, many=True,context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(len(wish_list_obj), status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def wish_list_delete(request):
    try:
        wish_list_obj=WishList.objects.get( Q(user_id=request.data['userid']) & Q(Product_id=request.data['Product']) & Q(isActive=1))
        wish_list_obj.delete()
        return Response("Deleted Successfully", status=status.HTTP_200_OK)
    except Exception:
        return Response("Not deleted successfully",  status=status.HTTP_200_OK)
   