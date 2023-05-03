from django.shortcuts import render, redirect,get_object_or_404
from restapiservice.models import Product,ProductImages
from django.contrib.auth.decorators import login_required
from ..forms import ProductImageForm
from ..decorator import user_is_admin


@login_required
@user_is_admin
def product_image_list(request):
    productimages=ProductImages.objects.all()
    return render(request, template_name='back/productimages/product_images_list.html',context={'productimages':productimages})


@login_required
@user_is_admin
def product_image_add(request):
    pd = Product.objects.all()
    saved = False

    if request.method == "POST":
        # Get the posted form
        MyProductImageForm = ProductImageForm(request.POST, request.FILES)
        if MyProductImageForm.is_valid():

            Imagefiles = request.FILES.getlist('pictures')
            for img in Imagefiles:
                if str(img).lower().endswith(('.png', '.jpg', '.jpeg')):
                    product_img_obj = ProductImages()
                    product_img_obj.product = MyProductImageForm.cleaned_data["product"]
                    product_img_obj.description = MyProductImageForm.cleaned_data["description"]
                    product_img_obj.isActive = bool(int(MyProductImageForm.cleaned_data["chkStatus"]))
                    print(img)
                    product_img_obj.ImageUrl = img
                    product_img_obj.save()

                    saved = True

    return render(request, template_name='back/productimages/product_images_add.html',context={'pd':pd})


@login_required
@user_is_admin
def product_image_delete(request,pk):
    product_img_obj=ProductImages.objects.filter(pk=pk)
    product_img_obj.delete()
    return redirect('productImagesList')


@login_required
@user_is_admin
def product_image_edit(request,pk):
    product_img_obj=ProductImages.objects.get(pk=pk)
    pd = Product.objects.all()
    edited = False
    # if pd.ImageUrl != '':
    #     print(pd.ImageUrl)

    if request.method == "POST":
        # Get the posted form
        MyProductImageForm = ProductImageForm(request.POST, request.FILES)
        print(request.POST,MyProductImageForm.is_valid())
        if MyProductImageForm.is_valid():
            product_img_obj.product = MyProductImageForm.cleaned_data["product"]
            product_img_obj.description = MyProductImageForm.cleaned_data["description"]
            product_img_obj.isActive = bool(int(MyProductImageForm.cleaned_data["chkStatus"]))
            if int(MyProductImageForm.cleaned_data["chkPrevImage"])==0 and MyProductImageForm.cleaned_data["pictures"]!=None:
                # print(MyProductImageForm.cleaned_data["pictures"])
                product_img_obj.ImageUrl = MyProductImageForm.cleaned_data["pictures"]
            product_img_obj.save()
            edited = True
        print(edited)
    return render(request, template_name='back/productimages/product_images_edit.html',context={'pk':pk,'productimages':product_img_obj,
                                                                                    'pd':pd})
