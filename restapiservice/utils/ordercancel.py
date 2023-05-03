from ..models import OrderInfo, OrderItemInfo,Product,TrackingInfo,OrderCancellationRequest
from .customlogger import customlogger

# def proceed_cancellation(orderid,comment):
#     cancel_flag=0
#     try:
#         cust=customlogger()
#         order_obj= OrderInfo.objects.get(id=orderid)
#         if order_obj.payment_status=="success":
#             if order_obj.payment_method=="cod":
#                 status_flag=update_order_tracking_status(orderid,"Cancelled",comment)
#                 if status_flag==1:
#                     stock_flag=update_stock_cancellation(orderid)
#                     cancel_flag=stock_flag 
#             elif order_obj.payment_method=="payu":
#                 # cancel status
#                 # stock upadation 
#                 # payu refund api
#                 pass
#             else:
#                 pass         
#     except Exception as e:
#         cust.loggerInfo.error(str(e))
#         cancel_flag = 0

#     return cancel_flag


def update_order_tracking_status(orderid,status,comment):
    update_flag=0
    try:
        cust=customlogger()
        track_order_obj= TrackingInfo.objects.get(order_id=orderid)
        if track_order_obj.status !="Dispatched" and track_order_obj.status !="Cancelled":
            track_order_obj.status=status
            track_order_obj.Comments= track_order_obj.Comments +"-----/n"+comment
            track_order_obj.save()
            update_flag=1
        else:
            update_flag = 0

    except Exception as e:
        cust.loggerInfo.error(str(e))
        update_flag = 0

    return update_flag


def update_stock_cancellation(orderid):
    update_flag=0
    try:
        cust=customlogger()
        all_items=OrderItemInfo.objects.filter(order_id=orderid)
        for products in all_items.iterator():
            prod_obj=Product.objects.get(id=products.product_id)
            prod_obj.quantity=prod_obj.quantity+products.quantity
            prod_obj.save()
        update_flag=1
    except Exception as e:
        cust.loggerInfo.error(str(e))
        update_flag = 0

    return update_flag

def proceed_cancellation_request(orderid,comment):
    cancel_flag=0
    try:
        cust=customlogger()
        order_obj= OrderInfo.objects.get(id=orderid)
        # create order cancellation request
        track_order_obj= TrackingInfo.objects.get(order_id=orderid)
        track_order_status=track_order_obj.status
        order_cancel_req_obj=OrderCancellationRequest(order=order_obj,comment=comment,request_status="Initiated",isActive=True,request_time_track_status=track_order_status)
        order_cancel_req_obj.save()
        track_order_obj.status = 'Cancellation Initiated'
        track_order_obj.save()
        cancel_flag=1
        # if order_obj.payment_status=="success":           
            # if order_obj.payment_method=="cod":
            #     pass
            # elif order_obj.payment_method=="payu":
            #     # create order cancellation request
            #     order_cancel_req_obj=OrderCancellationRequest(order=order_obj,comment=comment,request_status="Initiated",isActive=True)
            #     order_cancel_req_obj.save()
            #     cancel_flag=1                
            # else:
            #     pass         
    except Exception as e:
        cust.loggerInfo.error(str(e))
        cancel_flag = 0

    return cancel_flag

    
def confirm_cancellation_request_admin(orderid,comment):
    cancel_flag=0
    try:
        cust=customlogger()
        order_obj= OrderInfo.objects.get(id=orderid)
        if order_obj.payment_status=="success": 
            status_flag=update_order_tracking_status(orderid,"Cancelled",comment)
            if status_flag==1:
                stock_flag=update_stock_cancellation(orderid)
                cancel_flag=stock_flag          
            # if order_obj.payment_method=="cod":
            #     pass
            # elif order_obj.payment_method=="payu":
            #     # create order cancellation request
            #     status_flag=update_order_tracking_status(orderid,"Cancelled",comment)
            #     if status_flag==1:
            #         stock_flag=update_stock_cancellation(orderid)
            #         cancel_flag=stock_flag              
            # else:
            #     pass         
    except Exception as e:
        cust.loggerInfo.error(str(e))
        cancel_flag = 0

    return cancel_flag

def proceed_cancellation_request_admin(orderid,comment):
    cancel_flag=0
    try:
        cust=customlogger()
        order_obj= OrderInfo.objects.get(id=orderid)
        # create order cancellation request
        track_order_obj= TrackingInfo.objects.get(order_id=orderid)
        track_order_status=track_order_obj.status
        order_cancel_req_obj=OrderCancellationRequest(order=order_obj,comment=comment,request_status="Initiated",isActive=True,request_time_track_status=track_order_status)
        order_cancel_req_obj.save()
        cancel_flag=1               
    except Exception as e:
        cust.loggerInfo.error(str(e))
        cancel_flag = 0

    return cancel_flag