from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated
from restapiservice.serializers.userserializer import UserSerializer

from rest_framework import viewsets, status
from ..models import UserInfo,UserContact
from rest_framework.decorators import action
from rest_framework.response import Response
from ..utils.userinfo import get_userid_by_email
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (AllowAny,)
    # permission_classes_by_action = {'create': [IsAdminUser],
    #                                 'destroy': [IsAdminUser],
    #                                 'update': [IsAdminUser],
    #                                 'destroy': [IsAdminUser],
    #                                 'partial_update': [IsAdminUser],
    #                                 'list': [IsAdminUser],
    #                                 'retrieve':[IsAdminUser],
    #                                 'user_info_by_email':[IsAuthenticated]
    #                                 }
    permission_classes_by_action = {'create': [AllowAny],
                                    'destroy': [IsAdminUser],
                                    'update': [IsAdminUser],
                                    'destroy': [IsAdminUser],
                                    'partial_update': [IsAdminUser],
                                    'list': [IsAdminUser],
                                    'retrieve':[IsAdminUser],
                                    'user_info_by_email':[AllowAny]
                                    }                                
                                    
    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError as e: 
            return [permission() for permission in self.permission_classes]

    @action(detail=False, name='userEmail', methods=['post'])
    def user_info_by_email(self, request, *args, **kwargs):
        # http: // < my_url > / ?order_by = created
        # order_by = self.request.GET.get('order_by')
        resp = 'No data found'
        if 'email' in request.data.keys():
            try:
                user_obj = UserInfo.objects.get(email=request.data['email'])
                # user_contact_obj = UserContact.objects.filter(user=user_obj).first()
                user_contact_obj = UserContact.objects.filter(user=user_obj)
                resp = {
                    'id': user_obj.id,
                    'username': user_obj.username,
                    'firstname': user_obj.first_name,
                    'lastname': user_obj.last_name,
                    'email': user_obj.email,
                    'status': user_obj.isActive,
                    'dob': user_obj.date_of_birth,
                    'mob': user_obj.phone,
                    'contact': ''
                }
                if len(user_contact_obj) != 0:
                    resp['contact'] = {
                        'address1': user_contact_obj[0].address1,
                        'address2': user_contact_obj[0].address2,
                        'postalcode': user_contact_obj[0].postalcode,
                        'city': user_contact_obj[0].city
                    }

            except Exception:
                pass
        return Response(resp)




