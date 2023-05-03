from rest_framework import serializers
from ..utils import google
from ..utils.socialauth import register_social_user
from rest_framework.exceptions import AuthenticationFailed


class GoogleSocialAuthSerializer(serializers.Serializer):
    auth_token = serializers.CharField()

    def validate_auth_token(self, auth_token):
        user_data = google.Google.validate(auth_token)
        try:
            user_data['sub']
        except:
            raise serializers.ValidationError(
                'The token is invalid or expired. Please login again.'
            )

        # if user_data['aud'] != '656380664249-e8aserr9nb7vr77tiafr6unj7o6lffnj.apps.googleusercontent.com':
        #     raise AuthenticationFailed('oops, who are you?')
        if user_data['aud'] != '1098527521121-hfqo1r0vtbc3ofip09ds421ume4jisp6.apps.googleusercontent.com':
            raise AuthenticationFailed('oops, who are you?')

        user_id = user_data['sub']
        email = user_data['email']
        name = user_data['name']
        provider = 'google'
        first_name = user_data['given_name']
        last_name = user_data['family_name']

        return register_social_user(provider,user_id,email,name,first_name,last_name)