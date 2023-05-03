from django.shortcuts import render
from restapiservice.models import TrackingInfo
from django.contrib.auth.decorators import login_required
from ..forms import TrackingInfoForm
from restapiservice.utils.html2pdf import gen_invoice_info
from ..decorator import user_is_admin
from restapiservice.utils.ordercancel import proceed_cancellation_request_admin

@login_required
@user_is_admin
def track_pending_list(request):
    pending_orders=TrackingInfo.objects.filter(status='Pending')
    return render(request, template_name='back/trackorders/track_order_pending_list.html',context={'trackorders': pending_orders})


@login_required
@user_is_admin
def track_approved_list(request):
    approved_orders=TrackingInfo.objects.filter(status='Approved')
    return render(request, template_name='back/trackorders/track_order_approved_list.html',context={'trackorders': approved_orders})


@login_required
@user_is_admin
def track_dispatched_list(request):
    dispatched_orders=TrackingInfo.objects.filter(status='Dispatched')
    return render(request, template_name='back/trackorders/track_order_dispatched_list.html',context={'trackorders': dispatched_orders})


@login_required
@user_is_admin
def track_cancelled_list(request):
    cancelled_orders=TrackingInfo.objects.filter(status='Cancelled')
    return render(request, template_name='back/trackorders/track_order_cancelled_list.html',context={'trackorders': cancelled_orders})


@login_required
@user_is_admin
def track_cancelled_initiated_list(request):
    cancelled_initiated_orders=TrackingInfo.objects.filter(status='Cancellation Initiated')
    return render(request, template_name='back/trackorders/track_order_cancelled_initiated_list.html',context={'trackorders': cancelled_initiated_orders})

@login_required
@user_is_admin
def track_delivered_list(request):
    delivered_orders=TrackingInfo.objects.filter(status='Delivered')
    return render(request, template_name='back/trackorders/track_order_delivered_list.html',context={'trackorders': delivered_orders})


@login_required
@user_is_admin
def track_edit(request, pk):
    track_order_obj = TrackingInfo.objects.get(pk=pk)
    status_list=['Pending','Approved','Dispatched','Cancelled','Cancellation Initiated','Delivered']
    previous_order_status=track_order_obj.status
     # check whether any cancellation requests initiated for the current order cancellation,if no proceed cancellation
    if track_order_obj.status=="Cancellation Initiated":
        status_list=['Cancellation Initiated']
    if track_order_obj.status=="Pending":
        status_list.remove('Cancellation Initiated')
    
    if track_order_obj.status=="Approved":
        status_list.remove('Cancellation Initiated')
        status_list.remove('Pending')

    if track_order_obj.status=="Dispatched":
        status_list.remove('Cancellation Initiated')
        status_list.remove('Cancelled')
        status_list.remove('Pending')
        status_list.remove('Approved')
    
    if track_order_obj.status=="Cancelled":
        status_list.remove('Cancellation Initiated')
        status_list.remove('Dispatched')
        status_list.remove('Pending')
        status_list.remove('Approved')
    
    if track_order_obj.status=="Delivered":
        status_list=['Delivered']

    if request.method == "POST":
        myTrackingInfoForm = TrackingInfoForm(request.POST)
        if myTrackingInfoForm.is_valid():
            track_order_obj.Comments = myTrackingInfoForm.cleaned_data["comments"]
            track_order_obj.status = myTrackingInfoForm.cleaned_data["status"]
            
            if track_order_obj.status=="Dispatched":
                # mail generated invoice
                gen_invoice_info(pk)
            if track_order_obj.status=="Cancelled":               
                # create order cancellation from admin 
                order_cancel_status = proceed_cancellation_request_admin(track_order_obj.order.id,track_order_obj.Comments)
                if order_cancel_status == 1:
                    track_order_obj.status = 'Cancellation Initiated'
                else:
                    track_order_obj.status = previous_order_status
            track_order_obj.save()
    return render(request, template_name='back/trackorders/track_order_edit.html',context={'pk': pk,'trackOrder': track_order_obj, 'sl':status_list})