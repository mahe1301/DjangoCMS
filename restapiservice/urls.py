from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from . import views

# from .views import userauth
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

router=routers.DefaultRouter()
router.register('users',views.UserViewSet)
router.register('brands',views.BrandViewSet)
router.register('category',views.ProductCategoryViewSet)
router.register('products',views.ProductViewSet)

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('token/',views.MyTokenObtainPairView.as_view() ,name='token_obtain_pair'),
    path('token/refresh',views.MyTokenRefreshView.as_view(),name='token_refresh'),
    path('token/verify',views.MyTokenVerifyView.as_view(),name='token_verify'),
    path('account/', include(router.urls)),
    path('viewcartInfo', views.carthash),
    path('transaction/success',views.cartsuccess),
    path('transaction/failure',views.cartfailure),
    path('transaction/update',views.cartstatusupdate),
    
    path('user/orders/',views.user_orders),
    path('user/orders/items',views.user_order_items),
    path('user/orders/tracking',views.track_status),
    path('user/info/update', views.user_info_update),
    path('user/contact/update', views.user_contact_update),

    path('user/product/rating/list', views.customer_rating_list),
    path('user/product/rating/add', views.customer_rating_update),
    
    path('user/product/wishlist/update', views.wish_list_update),
    path('user/product/wishlist/list', views.wish_list_retrieve),
    path('user/product/wishlist/delete', views.wish_list_delete),
    
    path('product/specification/list', views.prod_spec_list),
    
    path('product/categorysearch/list', views.product_category),
    path('product/search/list', views.product_search),

    path('coupon/check', views.coupon_check),
    
    path('user/subscribe', views.customer_subscribe),
    path('user/order/cancel', views.order_cancel),
    path('auth/google/',views.Verify_google_user),
]

