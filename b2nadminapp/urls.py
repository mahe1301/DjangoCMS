from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.my_login,name="Login"),
    path('admin/', views.login_check,name="loginCheck"),
    path('logout/', views.my_logout,name="Logout"),
    path('users/list', views.user_list,name='userList'),

    path('home/', views.home,name='Home'),
    path('brands/list', views.brand_list,name='brandList'),
    path('brands/add', views.brand_add, name='brandAdd'),
    path('brands/delete/<int:pk>/',views.brand_delete, name='brandDelete'),
    path('brands/edit/<int:pk>/',views.brand_edit, name='brandEdit'),

    path('category/list', views.category_list,name='categoryList'),
    path('category/add', views.category_add, name='categoryAdd'),
    path('category/delete/<int:pk>/',views.category_delete, name='categoryDelete'),
    path('category/edit/<int:pk>/',views.category_edit, name='categoryEdit'),

    path('products/list', views.product_list,name='productList'),
    path('products/add', views.product_add, name='productAdd'),
    path('products/delete/<int:pk>/',views.product_delete, name='productDelete'),
    path('products/edit/<int:pk>/',views.product_edit, name='productEdit'),

    path('productimages/list', views.product_image_list,name='productImagesList'),
    path('productimages/add', views.product_image_add, name='productImagesAdd'),
    path('productimages/delete/<int:pk>/',views.product_image_delete, name='productImagesDelete'),
    path('productimages/edit/<int:pk>/',views.product_image_edit, name='productImagesEdit'),
    # path('login', views.login, name='login'),
    # path('loginCheck', views.user, name='loginCheck')

    path('purchaseorders/list', views.order_list,name='orderList'),
    path('purchaseorders/detail/<int:pk>/', views.order_detail,name='orderDetail'),
   
    path('trackorders/pending', views.track_pending_list, name='trackOrderPendingList'),
    path('trackorders/approved', views.track_approved_list, name='trackOrderApprovedList'),
    path('trackorders/dispatched', views.track_dispatched_list, name='trackOrderDispatchedList'),
    path('trackorders/cancelled', views.track_cancelled_list, name='trackOrderCancelledList'),
    path('trackorders/edit/<int:pk>/', views.track_edit, name='trackOrderEdit'),
    path('trackorders/cancelled_initiated', views.track_cancelled_initiated_list, name='trackOrderCancelledInitiatedList'),
    path('trackorders/delivered', views.track_delivered_list, name='trackOrderDeliveredList'),

    path('coupon/list', views.coupon_list, name='couponList'),
    path('coupon/add', views.coupon_add, name='couponAdd'),
    path('coupon/delete/<int:pk>/',views.coupon_delete, name='couponDelete'),
    path('coupon/edit/<int:pk>/',views.coupon_edit, name='couponEdit'),
    
    path('product/specification/category/list', views.specification_cat_list,name='specCategoryList'),
    path('product/specification/category/add', views.specification_cat_add, name='specCategoryAdd'),
    path('product/specification/category/delete/<int:pk>/', views.specification_cat_delete, name='specCategoryDelete'),
    path('product/specification/category/edit/<int:pk>/', views.specification_cat_edit, name='specCategoryEdit'),


    path('product/specification/list', views.product_spec_list,name='productSpecList'),
    path('product/specification/add', views.product_spec_add, name='productSpecAdd'),
    path('product/specification/delete/<int:pk>/', views.product_spec_delete, name='productSpecDelete'),
    path('product/specification/edit/<int:pk>/', views.product_spec_edit, name='productSpecEdit'),
    
    path('customer/subscription/list', views.customer_subscribe_list,name='subscribeList'),
    
    path('order/cancellation/requests/initiated', views.order_cancellation_initiated_list, name='orderCancelRequestInitiatedList'),
    path('order/cancellation/requests/pending', views.order_cancellation_pending_list, name='orderCancelRequestPendingList'),
    path('order/cancellation/requests/approved', views.order_cancellation_approved_list, name='orderCancelRequestApprovedList'),
    path('order/cancellation/requests/cancelled', views.order_cancellation_cancelled_list, name='orderCancelRequestCancelledList'),
    path('order/cancellation/requests/edit/<int:pk>/', views.order_cancellation_edit, name='orderCancelRequestEdit'),

]