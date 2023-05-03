from rest_framework import serializers

from ..models import UserInfo


class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model=UserInfo
        fields=['id','first_name','last_name','phone']