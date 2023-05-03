from django.shortcuts import render
from restapiservice.models import CouponInfo
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,get_object_or_404
from ..forms import CouponForm
from ..decorator import user_is_admin
from django.http import JsonResponse


@login_required
@user_is_admin
def coupon_list(request):
    coupons=CouponInfo.objects.all()
    return render(request, template_name='back/coupon/coupon_list.html',context={'coupons': coupons})


@login_required
@user_is_admin
def coupon_add(request):
    try:
        if request.method == "POST":
            my_coupon_form = CouponForm(request.POST)
            # print(request.POST)
            if my_coupon_form.is_valid():
                print('coupon_obj')
                coupon_obj = CouponInfo()
                coupon_obj.coupon_code = my_coupon_form.cleaned_data["couponcode"]
                coupon_obj.start_date = my_coupon_form.cleaned_data["startDate"]
                coupon_obj.end_date = my_coupon_form.cleaned_data["endDate"]
                coupon_obj.disc_percent = my_coupon_form.cleaned_data["discPercent"]
                coupon_obj.disc_min_order_amount = my_coupon_form.cleaned_data["discMinOrderAmount"]
                coupon_obj.disc_max_limit = my_coupon_form.cleaned_data["discMaxLimit"]
                coupon_obj.isActive = bool(int(my_coupon_form.cleaned_data["chkStatus"]))
                coupon_obj.save()
            # else:
            #     print('coupon_obj1')

    except Exception as e:
        print(e)
        return JsonResponse(e)
    finally:
        return render(request, template_name='back/coupon/coupon_add.html')


@login_required
@user_is_admin
def coupon_delete(request,pk):
    coupons_obj = CouponInfo.objects.filter(pk=pk)
    coupons_obj.delete()
    return redirect('couponList')


@login_required
@user_is_admin
def coupon_edit(request,pk):
    coupon_obj = CouponInfo.objects.get(pk=pk)
    edited = False
    if request.method == "POST":
        my_coupon_form = CouponForm(request.POST)
        if my_coupon_form.is_valid():
            coupon_obj.coupon_code = my_coupon_form.cleaned_data["couponcode"]
            coupon_obj.start_date = my_coupon_form.cleaned_data["startDate"]
            coupon_obj.end_date = my_coupon_form.cleaned_data["endDate"]
            coupon_obj.disc_percent = my_coupon_form.cleaned_data["discPercent"]
            coupon_obj.disc_min_order_amount = my_coupon_form.cleaned_data["discMinOrderAmount"]
            coupon_obj.disc_max_limit = my_coupon_form.cleaned_data["discMaxLimit"]
            coupon_obj.isActive = bool(int(my_coupon_form.cleaned_data["chkStatus"]))
            coupon_obj.save()
        else:
            print(my_coupon_form.is_valid())
    return render(request, template_name='back/coupon/coupon_edit.html',context={'pk': pk,'coupon': coupon_obj})