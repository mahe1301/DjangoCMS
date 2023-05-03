from rest_framework.permissions import AllowAny,IsAdminUser
from rest_framework.decorators import api_view,permission_classes

from django.http import HttpResponse
from ..utils.html2pdf import render_to_pdf,gen_invoice_info
from ..models import Product
from ..utils.customlogger import customlogger


# @api_view(["GET"])
# @permission_classes([AllowAny])
# def gen_invoice_pdf(request):
#     # getting the template
#     results=Product.objects.all()
#     pdf = render_to_pdf('front\invoiceGenTemplate.html',{
#                 'pagesize':'A4',
#                 'mylist': results,
#             })

#     # rendering the template
#     response= HttpResponse(pdf, content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'   # force to download file
#     return response


# @api_view(["GET"])
# @permission_classes([IsAdminUser])
# def gen_invoice_pdf(request):
#     pdf= gen_invoice_info(request.data['orderid'])
#     # rendering the template
#     response= HttpResponse(pdf, content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'   # force to download file
#     return response