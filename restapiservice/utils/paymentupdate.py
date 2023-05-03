from ..models import OrderInfo, OrderItemInfo,BillingAddress,Product,TrackingInfo
from .customlogger import customlogger

def create_order_details(pay_status,pay_amount,pay_coupon,pay_coupon_amt,user_type,user_id,bank_ref,payment_method,shipping_amount):
    id=0
    try:
        cust=customlogger()
        order_obj = OrderInfo()
        order_obj.payment_status = pay_status
        order_obj.payment_amount = pay_amount
        order_obj.coupon_code = pay_coupon
        order_obj.coupon_amount = pay_coupon_amt
        order_obj.userType = user_type
        order_obj.user = user_id
        order_obj.bank_reference = bank_ref
        order_obj.payment_method=payment_method
        order_obj.shipping_amount=shipping_amount
        order_obj.save()
        id = order_obj.id

    except Exception as e:
        id=0
        cust.loggerInfo.error(str(e))

    return id


def create_order_item_details(order_id,product_id,order_quantity,actual_amt,discount_amt,trans_ref_description):
    id=0
    try:
        cust=customlogger()
        order_item_obj = OrderItemInfo()
        order_item_obj.order_id = order_id
        order_item_obj.product_id = product_id
        order_item_obj.quantity = order_quantity
        order_item_obj.actual_amount = actual_amt
        order_item_obj.discount_amount = discount_amt
        order_item_obj.product_bill_amount = int(actual_amt)- int(discount_amt)
        order_item_obj.description = trans_ref_description
        order_item_obj.save()
        id = order_item_obj.id

    except Exception as e:
        cust.loggerInfo.error(str(e))
        id=0

    return id


def create_billing_details(order_id,received_json_address):
    id=0
    try:
        cust=customlogger()
        order_billing_obj = BillingAddress()
        order_billing_obj.order_id = order_id
        order_billing_obj.first_name = received_json_address['firstname']
        order_billing_obj.last_name = received_json_address['lastname']
        order_billing_obj.email = received_json_address['email']
        order_billing_obj.phone = received_json_address['number']
        order_billing_obj.address1 = received_json_address['add1']
        # order_billing_obj.address2 = received_json_address['email']
        order_billing_obj.postal_code= received_json_address['zip']
        order_billing_obj.city = received_json_address['city']
        # order_billing_obj.user_id
        order_billing_obj.save()
        id = order_billing_obj.id

    except Exception as e:
        cust.loggerInfo.error(str(e))
        id=0

    return id


def update_order_status(trans_ref,status,bank_ref_num):
    update_flag=0
    try:
        cust=customlogger()
        order_item_obj = OrderItemInfo.objects.filter(description=str(trans_ref))
        # order_obj=order_item_obj.order
        order_obj= OrderInfo.objects.get(id=order_item_obj[0].order_id)
        order_obj.payment_status=status
        order_obj.bank_reference=str(bank_ref_num)
        order_obj.save()
        update_flag=1
    except Exception as e:
        cust.loggerInfo.error(str(e))
        update_flag = 0

    return update_flag


def update_stock(trans_ref,status):
    update_flag=0
    try:
        cust=customlogger()
        all_items=OrderItemInfo.objects.filter(description=trans_ref)
        for products in all_items.iterator():
            prod_obj=Product.objects.get(id=products.product_id)
            prod_obj.quantity=prod_obj.quantity-products.quantity
            prod_obj.save()
        update_flag=1
    except Exception as e:
        cust.loggerInfo.error(str(e))
        update_flag = 0

    return update_flag


def update_order_status_from_api(trans_ref,status):
    update_flag=0
    try:
        cust=customlogger()
        order_item_obj = OrderItemInfo.objects.filter(description=trans_ref)
        # order_obj=order_item_obj.order
        order_obj= OrderInfo.objects.get(id=order_item_obj[0].order_id)
        if order_obj.payment_status=="Process started":
            order_obj.payment_status=status
            order_obj.save()
            update_flag=1
        else:
            update_flag = 0

    except Exception as e:
        cust.loggerInfo.error(str(e))
        update_flag = 0

    return update_flag


def create_tracking_info(trans_ref,status):
    create_flag = 0
    try:
        cust=customlogger()
        order_item_obj = OrderItemInfo.objects.filter(description=str(trans_ref))
        tracking_obj=TrackingInfo()
        tracking_obj.tracking_reference=str(order_item_obj[0].order_id)+str(order_item_obj[0].id)
        tracking_obj.status='Pending'
        tracking_obj.order_id=order_item_obj[0].order_id
        tracking_obj.save()
        create_flag=1
    except Exception as e:
        cust.loggerInfo.error(str(e))
        create_flag = 0
    return create_flag