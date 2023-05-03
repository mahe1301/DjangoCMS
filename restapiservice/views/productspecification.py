from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from ..models import ProductSpecification
from restapiservice.serializers import ProductSpecificationSerializer
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from ..permissions.userpermissions import IsBasicUser

@api_view(['POST'])
@permission_classes([IsBasicUser, ])
def prod_spec_list(request):
    spec_cat_list = ProductSpecification.objects.filter( Q(product_id=request.data['productid']) & Q(isActive=1)).values_list('category__name', flat=True).distinct()
    if len(spec_cat_list) != 0:
        prod_spec_list_obj = ProductSpecification.objects.filter( Q(product_id=request.data['productid']) & Q(isActive=1))
        catdict={}
        for spec_cat in spec_cat_list:
            serializer = ProductSpecificationSerializer(ProductSpecification.objects.filter( Q(product_id=request.data['productid']) & Q(isActive=1) & Q(category__name=spec_cat)), many=True)
            catdict[spec_cat]=serializer.data
        return Response(catdict, status=status.HTTP_200_OK)
    return Response(len(spec_cat_list), status=status.HTTP_400_BAD_REQUEST)