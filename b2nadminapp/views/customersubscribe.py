from django.shortcuts import render
from restapiservice.models import CustomerSubscribe
from django.contrib.auth.decorators import login_required
from ..decorator import user_is_admin

@login_required
@user_is_admin
def customer_subscribe_list(request):
    cust_subscribes=CustomerSubscribe.objects.filter(isActive=True)
    return render(request, template_name='back/customersubscribe/customer_subscribe_list.html',context={'custsubscribes': cust_subscribes})