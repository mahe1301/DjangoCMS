from django.shortcuts import render, redirect,get_object_or_404
from restapiservice.models import Product,ProductCategory,Brands
from django.contrib.auth.decorators import login_required
from ..forms import ProductForm
from ..decorator import user_is_admin

@login_required
@user_is_admin
def product_list(request):
    products=Product.objects.all()
    return render(request, template_name='back/products/product_list.html',context={'products':products})


@login_required
@user_is_admin
def product_add(request):
    cat = ProductCategory.objects.all()
    bd = Brands.objects.all()
    # saved = False

    if request.method == "POST":
        # Get the posted form
        MyProductForm = ProductForm(request.POST, request.FILES)
        if MyProductForm.is_valid():
            product_obj = Product()
            product_obj.name = MyProductForm.cleaned_data["name"]
            product_obj.img = MyProductForm.cleaned_data["picture"]
            product_obj.category = MyProductForm.cleaned_data["category"]
            product_obj.brands = MyProductForm.cleaned_data["brands"]
            product_obj.description = MyProductForm.cleaned_data["description"]
            product_obj.price = MyProductForm.cleaned_data["price"]
            product_obj.discountprice = MyProductForm.cleaned_data["discountprice"]
            product_obj.quantity = MyProductForm.cleaned_data["quantity"]
            product_obj.isActive = bool(int(MyProductForm.cleaned_data["chkStatus"]))
            product_obj.isTopSeller = bool(int(MyProductForm.cleaned_data["chkTopSellerStatus"]))
            product_obj.isComboProduct = bool(int(MyProductForm.cleaned_data["chkComboStatus"]))
            product_obj.gstPercent= float(MyProductForm.cleaned_data["fgstPercent"])
            product_obj.save()
            # saved = True


    return render(request, template_name='back/products/product_add.html',context={'cat':cat,'bd':bd})


@login_required
@user_is_admin
def product_delete(request,pk):
    product_obj=Product.objects.filter(pk=pk)
    product_obj.delete()
    return redirect('productList')


@login_required
@user_is_admin
def product_edit(request,pk):
    product_obj=Product.objects.get(pk=pk)
    cat = ProductCategory.objects.all()
    bd = Brands.objects.all()
    edited = False

    if request.method == "POST":
        # Get the posted form
        MyProductForm = ProductForm(request.POST, request.FILES)
        print(request.POST)
        if MyProductForm.is_valid():
            print('test')
            product_obj.name = MyProductForm.cleaned_data["name"]
            # product_obj.img = MyProductForm.cleaned_data["picture"]
            product_obj.category = MyProductForm.cleaned_data["category"]
            product_obj.brands = MyProductForm.cleaned_data["brands"]
            product_obj.description = MyProductForm.cleaned_data["description"]
            product_obj.price = MyProductForm.cleaned_data["price"]
            product_obj.discountprice = MyProductForm.cleaned_data["discountprice"]
            product_obj.quantity = MyProductForm.cleaned_data["quantity"]
            product_obj.isActive = bool(int(MyProductForm.cleaned_data["chkStatus"]))
            product_obj.isTopSeller = bool(int(MyProductForm.cleaned_data["chkTopSellerStatus"]))
            product_obj.isComboProduct = bool(int(MyProductForm.cleaned_data["chkComboStatus"]))
            product_obj.gstPercent= float(MyProductForm.cleaned_data["fgstPercent"])
            if int(MyProductForm.cleaned_data["chkPrevImage"])==0 and MyProductForm.cleaned_data["picture"]!=None:
                # print(MyProductImageForm.cleaned_data["pictures"])
                product_obj.img = MyProductForm.cleaned_data["picture"]
            product_obj.save()
            # edited = True
        # print(edited)
    return render(request, template_name='back/products/product_edit.html',context={'pk':pk,'product':product_obj,
                                                                                    'cat':cat,'bd':bd})
