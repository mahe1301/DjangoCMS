from rest_framework import serializers
# from django.contrib.auth.models import User,Group
from django.contrib.auth.hashers import make_password
from ..models import UserInfo

class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model=UserInfo
        fields=['username','password','first_name','last_name','email']
        extra_kwargs={ 'password': {'write_only':True, 'required':True}}

    # overiding builtin method for posting user details
    def create(self, validated_data):
        user = UserInfo.objects.create_user(**validated_data)
        return user


