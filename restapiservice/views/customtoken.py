from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
from  ..serializers.customTokenserializer import MyTokenObtainPairSerializer,MyTokenRefreshSerializer,MyTokenVerifySerializer
from rest_framework.response import Response
from rest_framework import  status

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class MyTokenRefreshView(TokenRefreshView):
    serializer_class = MyTokenRefreshSerializer

class MyTokenVerifyView(TokenVerifyView):
    serializer_class = MyTokenVerifySerializer
    
    def post(self, request, *args, **kwargs):
        
        try:
            resp = super().post(request, *args, **kwargs)
            return resp
        except Exception as e:
            # resp={'detail': e.args[0],} 
            resp={'detail': e.args[0],'code':'not_valid'} 
            return Response(resp,status.HTTP_200_OK)