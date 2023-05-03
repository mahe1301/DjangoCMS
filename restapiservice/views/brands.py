from rest_framework.permissions import AllowAny, IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from restapiservice.serializers.brandserializer import BrandSerializer
from rest_framework import viewsets, status
from ..models import Brands, Product
from ..permissions.userpermissions import IsBasicUser
from restapiservice.serializers.productserializer import ProductSerializer
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brands.objects.all()
    serializer_class = BrandSerializer
    # permission_classes = (AllowAny,)

    permission_classes_by_action = {'create': [IsAdminUser],
                                    'destroy': [IsAdminUser],
                                    'update': [IsAdminUser],
                                    'destroy': [IsAdminUser],
                                    'partial_update': [IsAdminUser],
                                    'list': [IsBasicUser],
                                    'retrieve':[IsAdminUser],
                                    'brand_products':[IsBasicUser]
                                    }

    def create(self, request, *args, **kwargs):
        pass

    def destroy(self, request, *args, **kwargs):
        pass

    def update(self, request, *args, **kwargs):
        pass

    def partial_update(self, request, *args, **kwargs):
        pass

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError: 
            return [permission() for permission in self.permission_classes]

    # @action(detail=False,name='brandProducts')
    # def brand_products(self, request):
    #     products_obj = Product.objects.filter(brands_id=request.GET.get('brandid',0))
    #     page = self.paginate_queryset(products_obj)
    #     if page is not None:
    #         serializer = ProductSerializer(page, many=True)
    #         # return Response(serializer.data, status=status.HTTP_200_OK)
    #         return self.get_paginated_response(serializer.data)

    #     serializer = ProductSerializer(page, many=True)
    #     return Response(serializer.data)
    
    @action(detail=False,name='brandProducts', methods=['post'])
    def brand_products(self, request):
        resp = 'No data found'    
        if 'brandid' in request.data.keys():
            try:
                paginator = PageNumberPagination()
                prod_obj = Product.objects.filter(brands_id=int(request.data['brandid']))
                page = paginator.paginate_queryset(prod_obj, request)
                if page is not None:
                    serializer = ProductSerializer(page, many=True, context={'request': request})
                    return paginator.get_paginated_response(serializer.data)
                serializer = ProductSerializer(prod_obj, many=True, context={'request': request})
                return Response(serializer.data)
            except Exception as e:
                resp = str(e)
        return Response(resp)