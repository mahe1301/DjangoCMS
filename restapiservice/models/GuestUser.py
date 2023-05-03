from django.db import models

class GuestUser(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    email = models.CharField(verbose_name="email", max_length=60, unique=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    date_of_birth = models.DateField(verbose_name="date of birth", blank=True)
    date_modified = models.DateTimeField(db_column="date modified", auto_now=True)
    phone = models.CharField(max_length=15, blank=True)

    class Meta:
        db_table = 'GuestUser'