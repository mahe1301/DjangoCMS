from ..models import UserInfo


def get_userid_by_email(email):
    fetch_flag = 0
    try:
        user_obj = UserInfo.objects.get(email=str(email))
        fetch_flag=user_obj.id
    except Exception:
        fetch_flag = 0
    return fetch_flag