from django import forms
from restapiservice.models import ProductCategory,Brands

class ProductForm(forms.Form):
   name = forms.CharField(max_length = 100)
   picture = forms.ImageField(required=False)
   category = forms.ModelChoiceField(queryset=ProductCategory.objects.all())
   brands = forms.ModelChoiceField(queryset=Brands.objects.all())
   description = forms.CharField(max_length=255)
   price = forms.IntegerField()
   discountprice = forms.IntegerField(required=False)
   quantity = forms.IntegerField()
   chkStatus = forms.CharField(max_length=1)
   chkTopSellerStatus = forms.CharField(max_length=1)
   chkComboStatus = forms.CharField(max_length=1)
   chkPrevImage = forms.CharField(required=False)
   fgstPercent = forms.DecimalField(required=False)
   # , required = False
