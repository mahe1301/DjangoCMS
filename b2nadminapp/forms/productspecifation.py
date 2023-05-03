from django import forms
from restapiservice.models import Product,SpecificationCategory


class ProductSpecForm(forms.Form):
    specname = forms.CharField()
    specvalue = forms.CharField()
    product = forms.ModelChoiceField(queryset=Product.objects.all())
    category= forms.ModelChoiceField(queryset=SpecificationCategory.objects.all())
    chkStatus = forms.CharField(max_length=1)
