# Generated by Django 3.1 on 2020-10-07 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapiservice', '0006_auto_20201004_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderinfo',
            name='payment_method',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
