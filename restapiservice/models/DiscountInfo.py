from django.db import models
from . import DiscountCategoryInfo


class DiscountInfo(models.Model):
    category = models.ForeignKey(DiscountCategoryInfo, on_delete=models.PROTECT)
    created = models.DateTimeField(db_column="created date",auto_now_add=True, blank=True)
    modified = models.DateTimeField(db_column="modified date", auto_now=True)
    start_date = models.DateField(verbose_name="start date", blank=False)
    end_date = models.DateField(verbose_name="end date", blank=False)
    isActive = models.BooleanField(default=False)
    referenceIDs=models.CharField(max_length=255)

    class Meta:
        db_table = 'DiscountInfo'