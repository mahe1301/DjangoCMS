from rest_framework.permissions import AllowAny,IsAdminUser
from rest_framework.response import Response
from restapiservice.serializers.productcategoryserializer import ProductCategorySerializer
from rest_framework import viewsets, status
from ..models import ProductCategory
from ..permissions.userpermissions import IsBasicUser

class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    permission_classes_by_action = {'create': [IsAdminUser],
                                    'destroy': [IsAdminUser],
                                    'update': [IsAdminUser],
                                    'destroy': [IsAdminUser],
                                    'partial_update': [IsAdminUser],
                                    'list': [IsBasicUser],
                                    'retrieve':[IsBasicUser]
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