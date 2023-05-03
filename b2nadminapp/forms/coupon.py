from django import forms
from django.conf import settings

from restapiservice.models import CouponInfo


class CouponForm(forms.Form):
    couponcode=forms.CharField(max_length=255)
    startDate = forms.DateField(required=False, input_formats=settings.DATE_INPUT_FORMATS)
    endDate = forms.DateField(required=False, input_formats=settings.DATE_INPUT_FORMATS)
    discPercent = forms.IntegerField()
    discMinOrderAmount = forms.IntegerField()
    discMaxLimit = forms.IntegerField()
    chkStatus = forms.CharField(max_length=1)

