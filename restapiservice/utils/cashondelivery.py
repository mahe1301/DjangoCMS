from ..models import OrderInfo, OrderItemInfo,BillingAddress,Product,TrackingInfo
from .paymentupdate import update_stock,create_tracking_info,update_order_status
from .customlogger import customlogger

def update_cod_order_details(txnid,status,bank_ref_num):
    update_flag=0
    try:
        cust=customlogger()
        check_update=update_order_status(txnid,status,bank_ref_num)
        if check_update == 1:
            update_stock(txnid, status)
            create_tracking_info(txnid, status)
            update_flag=1
    except Exception as e:
        cust.loggerInfo.error(str(e))
        update_flag=0

    return update_flag