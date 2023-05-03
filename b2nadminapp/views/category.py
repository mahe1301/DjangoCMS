from django.shortcuts import render, redirect,get_object_or_404
from restapiservice.models import ProductCategory
from django.contrib.auth.decorators import login_required
from ..decorator import user_is_admin


@login_required(login_url='/b2n/')
@user_is_admin
def category_list(request):
    categories=ProductCategory.objects.all()
    return render(request, template_name='back/category/category_list.html',context={'categories':categories})

@login_required(login_url='/b2n/')
@user_is_admin
def category_add(request):
    if request.method == 'POST':
        txtname = request.POST['txtName']
        txtParentCategory = request.POST.get('txtParentCategory')
        isActive = request.POST.get('chkStatus')
        if isActive == "True":
            isActive = True
        else:
            isActive = False
        category_obj=ProductCategory(name=txtname,parentCategory=txtParentCategory,isActive=isActive)
        category_obj.save()
    return render(request, template_name='back/category/category_add.html')

@login_required(login_url='/b2n/')
@user_is_admin
def category_delete(request,pk):
    category_obj=ProductCategory.objects.filter(pk=pk)
    category_obj.delete()
    return redirect('categoryList')

@login_required(login_url='/b2n/')
@user_is_admin
def category_edit(request,pk):
    category_obj=ProductCategory.objects.get(pk=pk)

    if request.method == 'POST':
        txtname = request.POST.get('txtName')
        txtParentCategory = request.POST.get('txtParentCategory')
        isActive = request.POST.get('chkStatus')
        if isActive == "Active":
            isActive = True
        else:
            isActive = False
        category_obj.name=txtname
        category_obj.vendorInfo = txtParentCategory
        category_obj.isActive = isActive
        category_obj.save()
    return render(request, template_name='back/category/category_edit.html',context={'pk':pk,'category':category_obj})
