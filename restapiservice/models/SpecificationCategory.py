from django.db import models


class SpecificationCategory(models.Model):
    name = models.CharField(max_length=255,unique=True)
    isActive = models.BooleanField(default=True)

    class Meta:
        db_table = 'SpecificationCategory'