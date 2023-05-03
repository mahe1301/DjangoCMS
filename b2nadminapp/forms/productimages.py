from django import forms
from restapiservice.models import Product
from django.forms import ClearableFileInput,ImageField
from django.core.validators import validate_image_file_extension


class ProductImageForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all())
    description = forms.CharField(max_length=255)
    pictures = forms.ImageField(required = False)
    chkStatus = forms.CharField(max_length=1)
    chkPrevImage = forms.CharField(required = False)
    # widgets = {'pictures': ClearableFileInput(attrs={'multiple': True,'accept':'image/*'}),}
