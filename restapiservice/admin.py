from django.contrib import admin
from .models import UserInfo
from .models import Brands
from .models import Product
from .models import ProductCategory
from .models import ProductImages
# Register your models here.

admin.site.register(UserInfo)
admin.site.register(Brands)
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(ProductImages)

admin.site.site_header="B2N"




