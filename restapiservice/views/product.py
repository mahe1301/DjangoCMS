from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAdminUser
from rest_framework.pagination import PageNumberPagination
from restapiservice.serializers.productserializer import ProductSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import action
from django.db.models import Q
from ..models import Product
from ..permissions.userpermissions import IsBasicUser


class ProductViewSet(viewsets.ModelViewSet):
    #queryset = Product.objects.all()
    queryset = Product.objects.filter(isActive=True)
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination
    permission_classes_by_action = {'create': [IsAdminUser],
                                    'destroy': [IsAdminUser],
                                    'update': [IsAdminUser],
                                    'destroy': [IsAdminUser],
                                    'partial_update': [IsAdminUser],
                                    'list': [IsBasicUser],
                                    'retrieve':[IsBasicUser],
                                    'best_sellers':[IsBasicUser],
                                    'combo_products':[IsBasicUser]
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
        except KeyError as e: 
            return [permission() for permission in self.permission_classes]

    @action(detail=False,name='bestSellers')
    def best_sellers(self, request):
        # print("hello")
        recent_users = Product.objects.filter(isTopSeller=True)

        page = self.paginate_queryset(recent_users)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(recent_users, many=True)
        return Response(serializer.data)

    @action(detail=False,name='comboProducts')
    def combo_products(self, request):
        recent_users = Product.objects.filter(isComboProduct=True)

        page = self.paginate_queryset(recent_users)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(recent_users, many=True)
        return Response(serializer.data)

