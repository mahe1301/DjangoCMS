import hashlib
from rest_framework.permissions import AllowAny, IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
import json
from ..utils.paymentupdate import create_order_details,create_order_item_details,create_billing_details,update_order_status,update_stock,update_order_status_from_api,create_tracking_info
from ..utils.userinfo import get_userid_by_email
from ..utils.cashondelivery import update_cod_order_details 
from django.http import HttpResponseRedirect
from ..utils.customlogger import customlogger
from ..permissions.userpermissions import IsBasicUser
from ..utils.emailsender import sendEmailForOrderProcessing

@api_view(['POST'])
@permission_classes([IsBasicUser])
def carthash(request):
    
    try:
        cust=customlogger()
        data={'orderid': 0,'paymentmethod':"invalid"}
        MERCHANT_KEY = "vVOplqui"
        key = "vVOplqui"
        SALT = "sxAr39cEi0"
        # PAYU_BASE_URL = "https://sandboxsecure.payu.in/_payment"
        PAYU_BASE_URL = "https://secure.payu.in/_payment"
        # action="https://test.payu.in/_payment"
        posted = {}
        received_json_address = json.loads(request.POST['address'])
        received_json_products = json.loads(request.POST['products'])
        posted['amount']=request.POST['totalAmount']
        couponCode = request.POST['couponCode']
        couponAmount= request.POST['couponAmount']
        userType = request.POST['userType']
        paymentMethod = request.POST['paymentmethod']
        shippingAmount = request.POST['shipping']
        user =request.POST['user']              
        productlist = []
        order_id=0
        order_id = create_order_details("Process started", posted['amount'], couponCode, couponAmount,userType,user, 'NA',paymentMethod,shippingAmount)
        hash_object = hashlib.sha256(str(order_id).encode('utf-8'))
        txnid = hash_object.hexdigest()[0:20]
        hashh = ''
        posted['txnid'] = txnid
        # --------------
        if order_id!=0:
            for i in range(0,len(received_json_products)):
                productlist.append(str(received_json_products[i]['id'])+"-"+ str(received_json_products[i]['numbersInCart']) +
                            "-"+str(received_json_products[i]['price']))
                item_id=create_order_item_details(order_id, received_json_products[i]['id'], received_json_products[i]['numbersInCart'],
                                    received_json_products[i]['price'], received_json_products[i]['discountprice'],
                                    posted['txnid'])
                if item_id==0:
                    order_id = 0
            if order_id != 0:
                address_id=create_billing_details(order_id,received_json_address)
                if address_id==0:
                    order_id = 0
        # --------------
        if paymentMethod == "cod":
            if order_id != 0:
                chk_st = update_cod_order_details(txnid,'success','cash on delivery')
                if chk_st == 0:
                    order_id = 0
            data={'orderid': order_id,'paymentmethod':paymentMethod}
            return Response(data)

        # ---------
        product_string= ','.join(productlist)
        posted['firstname'] = received_json_address['firstname']
        posted['email'] = received_json_address['email']
        posted['productinfo'] = product_string
        hashSequence = "key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10"
        posted['key'] = key
        hash_string = ''
        hashVarsSeq = hashSequence.split('|')
        for i in hashVarsSeq:
            try:
                hash_string += str(posted[i])
            except Exception as e:
                cust.loggerInfo.error(str(e))
                hash_string += ''
                # order_id = 0
            hash_string += '|'
        hash_string += SALT
        hashh = hashlib.sha512(hash_string.encode('utf-8')).hexdigest().lower()
        action = PAYU_BASE_URL #action="https://test.payu.in/_payment"
        data = {
            'posted': posted,
            'hashh': hashh,
            'MERCHANT_KEY': MERCHANT_KEY,
            'txnid': txnid,
            'hash_string': hash_string,
            'action': action,
            'orderid': order_id,
            'paymentmethod':paymentMethod
        }
    except Exception as e:
        cust.loggerInfo.error(str(e))
    finally:
        return Response(data)
        

    



@api_view(['POST'])
@permission_classes([AllowAny])
def cartsuccess(request):
    try:
        cust=customlogger()
        msg = "NA"
        status = request.POST["status"]
        firstname = request.POST["firstname"]
        amount = request.POST["amount"]
        txnid = request.POST["txnid"]
        posted_hash = request.POST["hash"]
        key = request.POST["key"]
        productinfo = request.POST["productinfo"]
        email = request.POST["email"]
        bank_ref_num=request.POST["bank_ref_num"]
        salt = "sxAr39cEi0"
        try:
            additionalCharges = request.POST["additionalCharges"]
            retHashSeq = additionalCharges + '|' + salt + '|' + status + '|||||||||||' + email + '|' + firstname + '|' + productinfo + '|' + amount + '|' + txnid + '|' + key
        except Exception as e:
            cust.loggerInfo.error(str(e))
            retHashSeq = salt + '|' + status + '|||||||||||' + email + '|' + firstname + '|' + productinfo + '|' + amount + '|' + txnid + '|' + key
        hashh = hashlib.sha512(retHashSeq.encode('utf-8')).hexdigest().lower()
        if hashh != posted_hash:
            msg = "Invalid Transaction. Please try again"
        else:
            msg = "Thank You. Your order status is "+ status
            msg += "Your Transaction ID for this transaction is " + str(txnid)
            # save status to db
            # cust.loggerInfo.info("Starting to save status in database for transaction: "+ str(txnid) + "---+ status :"+ str(status)+ "---+ bank ref :"+ str(bank_ref_num))
            check_update=update_order_status(txnid,status,bank_ref_num)
            if check_update == 1:
                # msg += "We have received a payment of Rs. " + amount + ". Your order will soon be shipped."
                msg += "We have received a payment of Rs.. Your order will soon be shipped."
                update_stock(txnid, status)
                create_tracking_info(txnid, status)
                # send email notification to customers for successfull payments
                html_content = """
                        <html>
                        <head></head>
                        <body>
                            <p>Hi {0} <br></p>
                            <p>Your order has been successfully placed.
                            </p>
                            <p>Your Transaction ID for this transaction is {1} .
                            </p>
                            <p>
                            Regards,</p>
                            <p>B2N Team
                            </p>
                        </body>
                        </html>
                    """.format(ofirstname,str(txnid))               
                e_subject = "Order Successfull"
                email_to = [email]
                email_from = settings.EMAIL_HOST_USER
                email_bcc =["mahe78611@gmail.com"]
                mail_send=sendEmailForOrderProcessing(e_subject,html_content,email_to,email_from,email_bcc)
            else:
                msg += "Please contact back2nature regarding your shipment."
            # cust.loggerInfo.info("Ending  save status in database for transaction: "+ str(txnid) + "---+ status :"+ str(status)+ "---+ bank ref :"+ str(bank_ref_num))
    except Exception as e:
        cust.loggerInfo.error(str(e))
    #---------------------
    finally:
        url='https://b2nnetwork.com/success?msg='+msg
        return HttpResponseRedirect(redirect_to=url)


@api_view(['POST'])
@permission_classes([AllowAny])
def cartfailure(request):
    try:
        cust=customlogger()
        msg = "NA"
        status = request.POST["status"]
        firstname = request.POST["firstname"]
        amount = request.POST["amount"]
        txnid = request.POST["txnid"]
        posted_hash = request.POST["hash"]
        key = request.POST["key"]
        productinfo = request.POST["productinfo"]
        email = request.POST["email"]
        bank_ref_num = request.POST["bank_ref_num"]
        salt = "sxAr39cEi0"
        try:
            additionalCharges = request.POST["additionalCharges"]
            retHashSeq = additionalCharges + '|' + salt + '|' + status + '|||||||||||' + email + '|' + firstname + '|' + productinfo + '|' + amount + '|' + txnid + '|' + key
        except Exception as e:
            cust.loggerInfo.error(str(e))
            retHashSeq = salt + '|' + status + '|||||||||||' + email + '|' + firstname + '|' + productinfo + '|' + amount + '|' + txnid + '|' + key
        hashh = hashlib.sha512(retHashSeq.encode('utf-8')).hexdigest().lower()
        if hashh != posted_hash:
            msg = "Invalid Transaction. Please try again"
        else:
            msg = "Thank You. Your order status is ", status
            cust.loggerInfo.info("Starting Failure status in database for transaction: "+ str(txnid) + "---+ status :"+ str(status)+ "---+ bank ref :"+ str(bank_ref_num))
            check_update = update_order_status(txnid, status, bank_ref_num)
            cust.loggerInfo.info("Ending Failure status in database for transaction: "+ str(txnid) + "---+ status :"+ str(status)+ "---+ bank ref :"+ str(bank_ref_num))
    except Exception as e:
        cust.loggerInfo.error(str(e))
    
    #---------------------
    finally:
        url = 'https://b2nnetwork.com/failure?msg=' + msg
        return HttpResponseRedirect(redirect_to=url)

@api_view(['POST'])
@permission_classes([IsBasicUser])
def cartstatusupdate(request):
    try:
        cust=customlogger()
        msg="Not updated"
        txnid = request.POST["txnid"]
        status = request.POST["status"]
        cust.loggerInfo.info("Start  update status from api  in database for transaction: "+ str(txnid) + "---+ status :"+ str(status))
        check_update = update_order_status_from_api(txnid,status)
        cust.loggerInfo.info("End  update status from api  in database for transaction: "+ str(txnid) + "---+ status :"+ str(status))
        if check_update == 1:
            msg="updated successfully"
    except:
        cust.loggerInfo.error(str(e))
    finally:
        data = {
            'msg': msg
        }
        return Response(data)