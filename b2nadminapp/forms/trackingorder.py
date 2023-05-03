from django import forms
from django.conf import settings

from restapiservice.models import TrackingInfo


class TrackingInfoForm(forms.Form):
    comments = forms.CharField(max_length=255)
    status = forms.CharField(max_length=255)