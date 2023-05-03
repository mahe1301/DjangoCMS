# from django.core.mail import send_mail
# from django.conf import settings
# from django.http import HttpResponseRedirect
# from rest_framework.response import Response
# from ..utils.emailsender import sendSimpleEmail
# from rest_framework.permissions import AllowAny, IsAuthenticated
# from rest_framework.decorators import api_view, permission_classes
# from django.shortcuts import  redirect
# from ..utils.customlogger import customlogger

# @api_view(['POST'])
# @permission_classes([AllowAny, ])
# def mailcustomer(request):
#     try:
#         cust=customlogger()
#         if 'sub' in request.data.keys() and 'msg' in request.data.keys() and 'email_to' in request.data.keys() :    
#             sub = request.data['sub']
#             msg = request.data['msg']
#             email_from = settings.EMAIL_HOST_USER
#             email_to = [request.data['email_to']]
#             res = sendSimpleEmail(sub,msg,email_to,email_from)
#     except Exception as e:
#         res='invalid'
#         cust.loggerInfo.error(str(e))
#     return Response(res)
