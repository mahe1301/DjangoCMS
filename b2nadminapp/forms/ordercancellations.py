from django import forms
from django.conf import settings

from restapiservice.models import OrderCancellationRequest


class OrderCancellationRequestInfoForm(forms.Form):
    comments = forms.CharField(max_length=255)
    status = forms.CharField(max_length=255)
    refundId = forms.IntegerField(required=False)
    refundStatus = forms.CharField(max_length=255,required=False)