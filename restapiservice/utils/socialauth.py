from django.contrib.auth import authenticate
# from django.contrib.auth.models import User
from ..models import UserInfo
import os
import random
from rest_framework.exceptions import AuthenticationFailed

SOCIAL_SECRET="1wdvefbqazrgn"

def generate_username(name):

    username = "".join(name.split(' ')).lower()
    if not UserInfo.objects.filter(username=username).exists():
        return username
    else:
        random_username = username + str(random.randint(0, 1000))
        return generate_username(random_username)


def register_social_user(provider, user_id, email, name,first_name,last_name):
    filtered_user_by_email = UserInfo.objects.filter(email=email)

    if filtered_user_by_email.exists():
        if provider == filtered_user_by_email[0].auth_provider:
            registered_user = authenticate(email=email, password=SOCIAL_SECRET)

            return {
                'username': registered_user.username,
                'email': registered_user.email,
                'tokens': registered_user.tokens()}

        else:
            raise AuthenticationFailed(
                detail='Please continue your login using ' + filtered_user_by_email[0].auth_provider)

    else:
        user = {
            'username': generate_username(name), 'email': email,'first_name':first_name,'last_name':last_name,
            'password': SOCIAL_SECRET}
        user = UserInfo.objects.create_user(**user)
        user.auth_provider = provider
        user.save()

        new_user = authenticate(
            email=email, password=SOCIAL_SECRET)
        return {
            'email': new_user.email,
            'username': new_user.username,
            'tokens': new_user.tokens()
        }