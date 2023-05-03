from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from ..models import Product
from restapiservice.serializers import ProductSerializer
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from ..permissions.userpermissions import IsBasicUser


@api_view(['POST'])
@permission_classes([IsBasicUser, ])
def product_category(request):
    resp = 'No data found'   
    if 'categoryid' in request.data.keys():
        try:
            paginator = PageNumberPagination()
            prod_obj = Product.objects.filter(category_id=int(request.data['categoryid']))
            page = paginator.paginate_queryset(prod_obj, request)
            if page is not None:
                serializer = ProductSerializer(page, many=True, context={'request': request})
                return paginator.get_paginated_response(serializer.data)
            serializer = ProductSerializer(prod_obj, many=True, context={'request': request})
            return Response(serializer.data)
        except Exception as e:
            resp = str(e)
    return Response(resp)

    
@api_view(['POST'])
@permission_classes([IsBasicUser, ])
def product_search(request):
    resp = 'No data found'
    if 'searchdetail' in request.data.keys():
        try:
            paginator = PageNumberPagination()
            prod_obj = Product.objects.filter( Q(category__name__icontains=request.data['searchdetail']) | Q(name__icontains=request.data['searchdetail']))
            page = paginator.paginate_queryset(prod_obj, request)
            if page is not None:
                serializer = ProductSerializer(page, many=True, context={'request': request})
                return paginator.get_paginated_response(serializer.data)
            serializer = ProductSerializer(prod_obj, many=True, context={'request': request})
            return Response(serializer.data)
        except Exception:
            pass
    return Response(resp)