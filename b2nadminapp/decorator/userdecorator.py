from django.core.exceptions import PermissionDenied
from restapiservice.models import UserInfo


def user_is_admin(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_anonymous:
            # print(request.user.is_anonymous)
            raise PermissionDenied
        else:
            # print(request.user,request.user.isActive,request.user.isAdmin,request.user.isStaff)
            if request.user.isActive and request.user.isAdmin:
                return function(request, *args, **kwargs)
            else:
                raise PermissionDenied

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap