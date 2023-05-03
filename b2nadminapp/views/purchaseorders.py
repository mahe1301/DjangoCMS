from django.shortcuts import render
from restapiservice.models import OrderInfo,OrderItemInfo,BillingAddress
from django.contrib.auth.decorators import login_required
from ..decorator import user_is_admin

@login_required
@user_is_admin
def order_list(request):
    # orders=OrderInfo.objects.all()
    orders=OrderInfo.objects.extra(
        select={
            'trans_ref': 'SELECT DISTINCT description FROM OrderItemInfo WHERE OrderItemInfo.order_id = OrderInfo.id'
        },
    )
    print(orders)
    return render(request, template_name='back/purchaseorder/order_list.html',context={'orders':orders})

@login_required
@user_is_admin
def order_detail(request,pk):
    order_obj=OrderInfo.objects.get(pk=pk)
    order_items_obj = OrderItemInfo.objects.filter(order_id=order_obj.id)
    order_billing_obj = BillingAddress.objects.filter(order_id=order_obj.id)
    print(order_billing_obj[0].id)
    return render(request, template_name='back/purchaseorder/order_detail.html',context={'pk':pk,'order':order_obj,
                                                                                    'products':order_items_obj,
                                                                                         'address':order_billing_obj[0]})