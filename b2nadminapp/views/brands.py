from django.shortcuts import render, redirect,get_object_or_404
from restapiservice.models import Brands
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from ..decorator import user_is_admin


# def email_check(user):
#     return user.email.endswith('@example.com')
#
#
# @user_passes_test(email_check, login_url='/b2n/')
# def sample(request):
#     return redirect('Login')

@login_required(login_url='/b2n/')
@user_is_admin
def brand_list(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    brands=Brands.objects.all()
    return render(request, template_name='back/brands/brands_list.html',context={'brands':brands})


@login_required(login_url='/b2n/')
@user_is_admin
def brand_add(request):
    if request.method == 'POST':
        txtname = request.POST['txtName']
        txtVendor = request.POST.get('txtVendor')
        isActive = request.POST.get('chkStatus')
        # print(len(txtname),txtname, txtVendor, isActive)
        # if txtname=='' or txtVendor == '' or len(txtname) == 0 or len(txtVendor) == 0 :
        #     errormsg = "Fields are required"
        #     render(request, template_name='back/error.html', context={'errormsg': errormsg})

        if isActive == "True":
            isActive = True
        else:
            isActive = False
        # print(txtname,txtVendor,isActive)
        brand_obj=Brands(name=txtname,vendorInfo=txtVendor,isActive=isActive)
        brand_obj.save()
    return render(request, template_name='back/brands/brands_add.html')


@login_required(login_url='/b2n/')
@user_is_admin
def brand_delete(request,pk):
    brand_obj=Brands.objects.filter(pk=pk)
    brand_obj.delete()
    return redirect('brandList')


@login_required(login_url='/b2n/')
@user_is_admin
def brand_edit(request,pk):
    brand_obj=Brands.objects.get(pk=pk)

    if request.method == 'POST':
        txtname = request.POST.get('txtName')
        txtVendor = request.POST.get('txtVendor')
        isActive = request.POST.get('chkStatus')
        # print(txtname, txtVendor, isActive)
        # if txtname == '' or txtVendor == '':
        #     errormsg = "Fields are required"
        #     render(request, template_name='back/error.html',context={'errormsg':errormsg})
        if isActive == "Active":
            isActive = True
        else:
            isActive = False
        brand_obj.name=txtname
        brand_obj.vendorInfo = txtVendor
        brand_obj.isActive = isActive
        brand_obj.save()
        # print(request.POST,isActive)
    return render(request, template_name='back/brands/brands_edit.html',context={'pk':pk,'brand':brand_obj})
