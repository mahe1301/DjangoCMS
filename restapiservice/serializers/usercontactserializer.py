from ..models import UserContact
from rest_framework import serializers


class UserContactSerializer(serializers.ModelSerializer):

    class Meta:
        model=UserContact
        fields=['user','address1','address2','postalcode','city']

