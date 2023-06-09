# Generated by Django 3.1 on 2020-09-25 17:28

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import restapiservice.utils.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=70, unique=True)),
                ('first_name', models.CharField(max_length=70)),
                ('last_name', models.CharField(max_length=70)),
                ('email', models.CharField(max_length=60, unique=True, verbose_name='email')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('isActive', models.BooleanField(default=True)),
                ('isStaff', models.BooleanField(default=False)),
                ('isAdmin', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('date_of_birth', models.DateField(blank=True, default=django.utils.timezone.now, verbose_name='date of birth')),
                ('date_modified', models.DateTimeField(auto_now=True, db_column='date modified')),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'UserAccount',
            },
        ),
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('vendorInfo', models.CharField(blank=True, max_length=255, null=True)),
                ('isActive', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'Brands',
            },
        ),
        # migrations.CreateModel(
        #     name='CouponInfo',
        #     fields=[
        #         ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('created', models.DateTimeField(auto_now_add=True, db_column='created date')),
        #         ('modified', models.DateTimeField(auto_now=True, db_column='modified date')),
        #         ('start_date', models.DateField(blank=True, verbose_name='start date')),
        #         ('end_date', models.DateField(blank=True, verbose_name='end date')),
        #         ('disc_percent', models.FloatField(blank=True)),
        #         ('disc_min_order_amount', models.IntegerField(blank=True)),
        #         ('disc_max_limit', models.IntegerField(blank=True)),
        #         ('isActive', models.BooleanField(default=False)),
        #     ],
        #     options={
        #         'db_table': 'CouponInfo',
        #     },
        # ),
        migrations.CreateModel(
            name='GuestUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=70)),
                ('last_name', models.CharField(max_length=70)),
                ('email', models.CharField(max_length=60, unique=True, verbose_name='email')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('date_of_birth', models.DateField(blank=True, verbose_name='date of birth')),
                ('date_modified', models.DateTimeField(auto_now=True, db_column='date modified')),
                ('phone', models.CharField(blank=True, max_length=15)),
            ],
            options={
                'db_table': 'GuestUser',
            },
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_column='created date')),
                ('modified', models.DateTimeField(auto_now=True, db_column='modified date')),
                ('payment_status', models.TextField()),
                ('payment_amount', models.IntegerField()),
                ('coupon_code', models.CharField(max_length=30)),
                ('coupon_amount', models.IntegerField(blank=True, null=True)),
                ('userType', models.CharField(blank=True, max_length=30, null=True)),
                ('user', models.TextField(blank=True, null=True)),
                ('bank_reference', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'OrderInfo',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('imageUrl', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('discountprice', models.IntegerField(blank=True, null=True)),
                ('inCart', models.BooleanField(default=False)),
                ('numbersInCart', models.IntegerField(default=0)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('isActive', models.BooleanField(default=True)),
                ('isTopSeller', models.BooleanField(default=True)),
                ('isComboProduct', models.BooleanField(default=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to=restapiservice.utils.image.upload_product)),
                ('brands', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='restapiservice.brands')),
            ],
            options={
                'db_table': 'Product',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('parentCategory', models.IntegerField(blank=True, null=True)),
                ('isActive', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'ProductCategory',
            },
        ),
        migrations.CreateModel(
            name='UserContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.CharField(max_length=255)),
                ('address2', models.CharField(blank=True, max_length=255)),
                ('postalcode', models.CharField(blank=True, max_length=15)),
                ('city', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'UserContact',
            },
        ),
        migrations.CreateModel(
            name='TrackingInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracking_reference', models.CharField(max_length=100, unique=True)),
                ('status', models.CharField(max_length=255)),
                ('Comments', models.CharField(max_length=255)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='restapiservice.orderinfo')),
            ],
            options={
                'db_table': 'TrackingInfo',
            },
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('ImageUrl', models.ImageField(blank=True, null=True, upload_to=restapiservice.utils.image.upload_product_images)),
                ('isActive', models.BooleanField(default=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='restapiservice.product')),
            ],
            options={
                'db_table': 'ProductImages',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='restapiservice.productcategory'),
        ),
        migrations.CreateModel(
            name='OrderItemInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True, db_column='created date')),
                ('actual_amount', models.IntegerField()),
                ('discount_amount', models.IntegerField()),
                ('product_bill_amount', models.IntegerField()),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='restapiservice.orderinfo')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='restapiservice.product')),
            ],
            options={
                'db_table': 'OrderItemInfo',
            },
        ),
        # migrations.CreateModel(
        #     name='CustomerRating',
        #     fields=[
        #         ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('created', models.DateTimeField(auto_now_add=True, db_column='created date')),
        #         ('modified', models.DateTimeField(auto_now=True, db_column='modified date')),
        #         ('rating', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
        #         ('description', models.TextField(blank=True)),
        #         ('Product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='restapiservice.product')),
        #         ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='restapiservice.orderinfo')),
        #         ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
        #     ],
        #     options={
        #         'db_table': 'CustomerRating',
        #     },
        # ),
        migrations.CreateModel(
            name='BillingAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=70)),
                ('last_name', models.CharField(max_length=70)),
                ('email', models.CharField(max_length=60, verbose_name='email')),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('address1', models.CharField(max_length=255)),
                ('address2', models.CharField(blank=True, max_length=255)),
                ('postal_code', models.CharField(blank=True, max_length=15)),
                ('city', models.CharField(max_length=100)),
                ('user_id', models.CharField(blank=True, max_length=15)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='restapiservice.orderinfo')),
            ],
            options={
                'db_table': 'BillingAddress',
            },
        ),
    ]
