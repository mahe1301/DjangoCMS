from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from ..decorator import user_is_admin
from restapiservice.models import Brands, Product, ProductImages, TrackingInfo, CustomerSubscribe, UserInfo
# Create your views here.


# def home(request):
#     data = '<html><body><h1>Hello, world</h1></body></html>'
#     return HttpResponse(data, content_type='text/plain')


@login_required(login_url='/b2n/')
@user_is_admin
def home(request):
     orderPendingCount=0
     orderApprovedCount=0
     orderCancelledCount=0
     orderDispatchedCount=0
     orderDeliveredCount=0
     brandCount=0
     productCount=0
     productImgCount=0
     subscriberCount=0
     registeredUserCount=0

     orderPendingCount=TrackingInfo.objects.filter(status='Pending').count()
     orderApprovedCount=TrackingInfo.objects.filter(status='Approved').count()
     orderCancelledCount=TrackingInfo.objects.filter(status='Cancelled').count()
     orderDispatchedCount=TrackingInfo.objects.filter(status='Dispatched').count()
     orderDeliveredCount=TrackingInfo.objects.filter(status='Delivered').count()
     brandCount=Brands.objects.filter(isActive=True).count()
     productCount=Product.objects.filter(isActive=True).count()
     productImgCount=ProductImages.objects.filter(isActive=True).count()
     subscriberCount=CustomerSubscribe.objects.filter(isActive=True).count()
     registeredUserCount=UserInfo.objects.filter(isActive=True).count()

     contextObj={'oPCount':orderPendingCount,'oACount':orderApprovedCount,'oCCount':orderCancelledCount,'oDispCount':orderDispatchedCount,'oDeliCount':orderDeliveredCount,'brandCount':brandCount,'productCount':productCount,'productImgCount':productImgCount,'subscriberCount':subscriberCount,'registeredUserCount':registeredUserCount}

     return render(request, template_name='back/home.html',context=contextObj)
