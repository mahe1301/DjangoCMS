from rest_framework import permissions
import base64


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.isActive and request.user.isAdmin:
            return True
        return False


class IsUserCustomer(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.isActive:
            return True
        return False


class IsBasicUser(permissions.BasePermission):
    def has_permission(self, request, view):
        req_origin="invalid"
        valid_origin='https://b2nnetwork.com'
        if 'HTTP_ORIGIN' in request.META:
            req_origin=request.META['HTTP_ORIGIN']
        if 'HTTP_AUTHORIZATION' in request.META and req_origin == valid_origin:
            auth = request.META['HTTP_AUTHORIZATION'].split()
            print(auth)
            if len(auth) == 2:
                if auth[0].lower() == "basic":
                    auth_string=str(base64.b64decode(auth[1]))
                    auth_string=auth_string[2:-1]
                    authlist = auth_string.split(':')
                    if authlist[0] == "tbest2Unamen" and authlist[1] == "tbest2basicpwdn":
                        return True

        return False