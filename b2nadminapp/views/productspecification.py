from django.shortcuts import render, redirect,get_object_or_404
from restapiservice.models import Product,ProductSpecification,SpecificationCategory
from django.contrib.auth.decorators import login_required
from ..forms import ProductSpecForm
from ..decorator import user_is_admin


@login_required
@user_is_admin
def product_spec_list(request):
    products_spec=ProductSpecification.objects.all()
    return render(request, template_name='back/productspecification/product_spec_list.html',context={'productspecs':products_spec})


@login_required
@user_is_admin
def product_spec_add(request):
    pd = Product.objects.all()
    speccat = SpecificationCategory.objects.all()
    if request.method == "POST":
        MyProductSpecForm = ProductSpecForm(request.POST)
        print(request.POST)
        if MyProductSpecForm.is_valid():
            product_spec_obj = ProductSpecification()
            product_spec_obj.name = MyProductSpecForm.cleaned_data["specname"]
            product_spec_obj.detail = MyProductSpecForm.cleaned_data["specvalue"]
            product_spec_obj.product = MyProductSpecForm.cleaned_data["product"]
            product_spec_obj.category = MyProductSpecForm.cleaned_data["category"]
            product_spec_obj.isActive = bool(int(MyProductSpecForm.cleaned_data["chkStatus"]))
            product_spec_obj.save()
        # else:
        #     print('hello')
    return render(request, template_name='back/productspecification/product_spec_add.html',context={'pd':pd,'speccat':speccat})


@login_required
@user_is_admin
def product_spec_delete(request,pk):
    product_spec_obj=ProductSpecification.objects.filter(pk=pk)
    product_spec_obj.delete()
    return redirect('productSpecList')


@login_required
@user_is_admin
def product_spec_edit(request,pk):
    product_spec_obj=ProductSpecification.objects.get(pk=pk)
    pd = Product.objects.all()
    speccat = SpecificationCategory.objects.all()
    print(product_spec_obj)
    if request.method == "POST":
        MyProductSpecForm = ProductSpecForm(request.POST)
        if MyProductSpecForm.is_valid():
            print('test')
            product_spec_obj.name = MyProductSpecForm.cleaned_data["specname"]
            product_spec_obj.detail = MyProductSpecForm.cleaned_data["specvalue"]
            product_spec_obj.product = MyProductSpecForm.cleaned_data["product"]
            product_spec_obj.category = MyProductSpecForm.cleaned_data["category"]
            product_spec_obj.isActive = bool(int(MyProductSpecForm.cleaned_data["chkStatus"]))
            product_spec_obj.save()
    return render(request, template_name='back/productspecification/product_spec_edit.html', context={'pk': pk, 'productspec': product_spec_obj, 'pd': pd,'speccat':speccat})