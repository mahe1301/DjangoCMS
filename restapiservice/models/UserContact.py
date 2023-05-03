from django.db import models
from . import UserInfo


class UserContact(models.Model):
    user = models.ForeignKey(UserInfo,on_delete=models.PROTECT)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255,blank=True)
    postalcode = models.CharField(max_length=15, blank=True)
    city = models.CharField(max_length=100)

    class Meta:
        db_table = 'UserContact'



