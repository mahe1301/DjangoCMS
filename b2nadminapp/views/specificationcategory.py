from django.shortcuts import render, redirect,get_object_or_404
from restapiservice.models import SpecificationCategory
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from ..decorator import user_is_admin



@login_required(login_url='/b2n/')
@user_is_admin
def specification_cat_list(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    spec_cat_obj=SpecificationCategory.objects.all()
    return render(request, template_name='back/specificationcategory/spec_cat_list.html',context={'speccat':spec_cat_obj})


@login_required(login_url='/b2n/')
@user_is_admin
def specification_cat_add(request):
    if request.method == 'POST':
        txtname = request.POST['txtName']
        isActive = request.POST.get('chkStatus')
        if isActive == "True":
            isActive = True
        else:
            isActive = False
        spec_cat_obj=SpecificationCategory(name=txtname,isActive=isActive)
        spec_cat_obj.save()
        return redirect('specCategoryList')
    return render(request, template_name='back/specificationcategory/spec_cat_add.html')


@login_required(login_url='/b2n/')
@user_is_admin
def specification_cat_delete(request,pk):
    spec_cat_obj=SpecificationCategory.objects.filter(pk=pk)
    spec_cat_obj.delete()
    return redirect('specCategoryList')


@login_required(login_url='/b2n/')
@user_is_admin
def specification_cat_edit(request,pk):
    spec_cat_obj=SpecificationCategory.objects.get(pk=pk)

    if request.method == 'POST':
        txtname = request.POST.get('txtName')
        isActive = request.POST.get('chkStatus')
        if isActive == "Active":
            isActive = True
        else:
            isActive = False
        spec_cat_obj.name=txtname
        spec_cat_obj.isActive = isActive
        spec_cat_obj.save()
        return redirect('specCategoryList')
    return render(request, template_name='back/specificationcategory/spec_cat_edit.html',context={'pk':pk,'speccat':spec_cat_obj})
