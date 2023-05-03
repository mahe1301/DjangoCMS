from io import BytesIO #A stream implementation using an in-memory bytes buffer  # It inherits BufferIOBase
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from .emailsender import sendEmailWithInvoice
from xhtml2pdf import pisa #pisa is a html2pdf converter using the ReportLab Toolkit, #the HTML5lib and pyPdf.
from django.conf import settings
from .customlogger import customlogger
from ..models import OrderInfo,OrderItemInfo,BillingAddress

from .invoicehelper import invoicehelper
from num2words import num2words
# from pathlib import Path

def render_to_pdf(template_src, context_dict):
     template_src1 = get_template(template_src)
     context = Context(context_dict)
     html = template_src1.render(context_dict)
     result = BytesIO()
     pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
     if not pdf.err:
         return HttpResponse(result.getvalue(), content_type='application/pdf')
     return None




def send_email_invoice_pdf(template_src, context_dict,invoice_name,e_subject,e_msg,email_to):
    try:
        res=0
        cust=customlogger()
        template_src1 = get_template(template_src)
        
        context = Context(context_dict)
        print(context)
        html = template_src1.render(context_dict)
        # print(html)
        output_filename=settings.MEDIA_ROOT+"/invoice/"+invoice_name+".pdf"   # for server
        # output_filename=settings.MEDIA_ROOT+"\\invoice\\"+invoice_name+".pdf" # for local
        result_file = open(output_filename, "w+b")
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result_file)
        result_file.close()
        if not pdf.err:
            # with open(output_filename, "rb") as f:
            #      res=f.read()
            email_from=settings.EMAIL_HOST_USER
            res=sendEmailWithInvoice(e_subject,e_msg,email_to,email_from,output_filename)
    except Exception as e:
        res=0
        cust.loggerInfo.error(str(e))
    return res


def gen_invoice_info(orderid):
    try:
        res=0
        cust=customlogger()
        cust.loggerInfo.info('invoice generation  started')
        template_src='front/invoiceb2nTemplate2.html'
        order_obj=OrderInfo.objects.get(pk=orderid)
        order_items_obj = OrderItemInfo.objects.filter(order_id=order_obj.id)
        order_billing_obj = BillingAddress.objects.get(order_id=order_obj.id)
        # print(order_billing_obj.id)
        # invoice calculation start
        order_items_obj_list=[]
        total_sgst=0
        total_cgst=0
        total_igst=0
        total=0
        discount_allowed=order_obj.coupon_amount
        if(len(order_items_obj) > 0):
            for i in range(len(order_items_obj)):
                invoice_obj=invoicehelper(i+1)
                invoice_obj.order_item=order_items_obj[i]
                invoice_obj.taxableamount = (invoice_obj.order_item.product_bill_amount * invoice_obj.order_item.quantity)
                if invoice_obj.order_item.product.gstPercent > 0:
                    gstsplit=( invoice_obj.order_item.product_bill_amount / invoice_obj.order_item.product.gstPercent) * 100
                    invoice_obj.sgst=gstsplit
                    invoice_obj.cgst=gstsplit
                    total_sgst = total_sgst + invoice_obj.sgst
                    total_cgst = total_cgst + invoice_obj.cgst
                else:
                    invoice_obj.sgst=0  
                    invoice_obj.cgst=0
                invoice_obj.product_total= invoice_obj.taxableamount + invoice_obj.sgst + invoice_obj.cgst
                total= total + invoice_obj.product_total 
                
                order_items_obj_list.append(invoice_obj)
        
        context_dict={
                'pagesize':'A4',
                'orderinfo': order_obj,
                'orderlist': order_items_obj_list,
                'billaddress':order_billing_obj,
                'totalsgst':total_sgst,
                'totalcgst':total_cgst,
                'totaligst':total_igst,
                'totalgstcollect':total_igst + total_cgst + total_sgst,
                'grandtotal':total - (total_igst + total_cgst + total_sgst), 
                'discountallowed':discount_allowed ,
                'netamount': total - discount_allowed, 
                'amountwords':num2words(total- discount_allowed).upper()
                
            }
        # invoice calculation end
        
        e_subject="Invoice"
        e_msg='''Dear Customer,
                 Please find your attached invoice for the order With id {orderid} placed successfully.
                 Regards,
                 B2N Team'''.format(orderid=order_obj.id)
        
        email_to=[order_billing_obj.email]
        invoice_name="invoiceref"+orderid
        # print(invoice_name)
        res=send_email_invoice_pdf(template_src, context_dict,invoice_name,e_subject,e_msg,email_to)
    except Exception as e:
        res=0
        cust.loggerInfo.error(str(e))
    return res

