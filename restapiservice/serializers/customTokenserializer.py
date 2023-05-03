from rest_framework_simplejwt.serializers import TokenObtainPairSerializer,TokenRefreshSerializer,TokenVerifySerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        # Add extra responses here
        data['username'] = self.user.username
        # data['groups'] = self.user.groups.values_list('name', flat=True)
        return data
    # @classmethod
    # def get_token(cls, user):
    #     token = super().get_token(user)

    #     # Add custom claims
    #     # token['username'] = 'user.username'
    #     # token.update({'id': self.user.id})
    #     print(user.username)
    #     # print(token.refresh)
    #     token['username'] = 'user.username'
    #     # Add more custom fields from your custom user model, If you have a
    #     # custom user model.
    #     # ...
    #     return token

class MyTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        return data

class MyTokenVerifySerializer(TokenVerifySerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        if len(data)==0:
            data['detail']="Token is valid"
            data['code']="valid"
        return data
