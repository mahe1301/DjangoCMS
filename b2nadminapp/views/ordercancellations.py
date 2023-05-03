from django.shortcuts import render
from restapiservice.models import OrderCancellationRequest, TrackingInfo, BillingAddress
from django.contrib.auth.decorators import login_required
from ..forms import OrderCancellationRequestInfoForm
from restapiservice.utils.html2pdf import gen_invoice_info
from ..decorator import user_is_admin
from django.db import transaction
from restapiservice.utils.ordercancel import confirm_cancellation_request_admin
from restapiservice.utils.emailsender import sendEmailForOrderProcessing
from django.conf import settings

@login_required
@user_is_admin
def order_cancellation_initiated_list(request):
    initiated_orders=OrderCancellationRequest.objects.filter(request_status='Initiated')
    return render(request, template_name='back/ordercancellations/order_cancellation_initiated_list.html',context={'orderscancellations': initiated_orders})


@login_required
@user_is_admin
def order_cancellation_pending_list(request):
    pending_orders=OrderCancellationRequest.objects.filter(request_status='Pending')
    return render(request, template_name='back/ordercancellations/order_cancellation_pending_list.html',context={'orderscancellations': pending_orders})


@login_required
@user_is_admin
def order_cancellation_approved_list(request):
    approved_orders=OrderCancellationRequest.objects.filter(request_status='Approved')
    return render(request, template_name='back/ordercancellations/order_cancellation_approved_list.html',context={'orderscancellations': approved_orders})


@login_required
@user_is_admin
def order_cancellation_cancelled_list(request):
    cancelled_orders=OrderCancellationRequest.objects.filter(request_status='Cancelled')
    return render(request, template_name='back/ordercancellations/order_cancellation_cancelled_list.html',context={'orderscancellations': cancelled_orders})


@login_required
@user_is_admin
def order_cancellation_edit(request, pk):
    order_cancel_req_obj = OrderCancellationRequest.objects.get(pk=pk)
    status_list=['Initiated','Pending','Approved','Cancelled']
    request_previous_status=order_cancel_req_obj.request_status
    
    if track_order_obj.status=="Approved":
        status_list.remove('Initiated')
        status_list.remove('Pending')
        status_list.remove('Cancelled')

    if track_order_obj.status=="Pending":
        status_list.remove('Initiated')
        status_list.remove('Cancelled')

    
    if track_order_obj.status=="Cancelled":
        status_list.remove('Initiated')
        status_list.remove('Pending')
        status_list.remove('Approved')


    if request.method == "POST":
        orderCancellationRequestInfoForm = OrderCancellationRequestInfoForm(request.POST)
        # print(orderCancellationRequestInfoForm.is_valid())
        if orderCancellationRequestInfoForm.is_valid(): 
            order_cancel_req_obj.comment = orderCancellationRequestInfoForm.cleaned_data["comments"]
            order_cancel_req_obj.request_status = orderCancellationRequestInfoForm.cleaned_data["status"]
            order_cancel_req_obj.refund_id = orderCancellationRequestInfoForm.cleaned_data["refundId"]
            order_cancel_req_obj.refund_status = orderCancellationRequestInfoForm.cleaned_data["refundStatus"]
            # print(order_cancel_req_obj.request_status)
            if order_cancel_req_obj.request_status=="Approved":
                # cancellation mail generation
                # update confirmed order status
                with transaction.atomic():
                    order_cancel_status = confirm_cancellation_request_admin(order_cancel_req_obj.order.id,order_cancel_req_obj.comment)
                    if order_cancel_status!=1:
                        order_cancel_req_obj.status = request_previous_status
            order_cancel_req_obj.save()
            if order_cancel_req_obj.request_status=="Cancelled":
                 track_order_obj = TrackingInfo.objects.get(order_id=orderid)
                 track_order_obj.status = order_cancel_req_obj.request_time_track_status 
                 track_order_obj.save()
            ## cancellation mail generation
            if order_cancel_req_obj.request_status=="Approved":
                order_billing_obj=BillingAddress.objects.get(order_id=order_cancel_req_obj.order.id)
                html_content = """
                        <html>
                        <head></head>
                        <body>
                            <p>Hi {0} <br></p>
                            </p>Your order with id: {1} has been cancelled.
                            </p>
                            <p>
                            Regards,</p>
                            <p>B2N Team
                            </p>
                        </body>
                        </html>
                    """.format(order_billing_obj.first_name,order_cancel_req_obj.order.id)
                e_subject = "Order Cancellation"
                email_to = [order_billing_obj.email]
                email_from = settings.EMAIL_HOST_USER
                email_bcc =["mahe78611@gmail.com"]
                mail_send=sendEmailForOrderProcessing(e_subject,html_content,email_to,email_from,email_bcc)
    return render(request, template_name='back/ordercancellations/order_cancellation_edit.html',context={'pk': pk,'orderscancellation': order_cancel_req_obj, 'sl':status_list})