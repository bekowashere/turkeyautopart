from django.urls import path, include

from base.api.views import ProductListAPIView, ProductDetailAPIView, ProductDeleteAPIView, ProductUpdateAPIView, ProductCreateAPIView

app_name = 'base'


urlpatterns = [
    path('products', ProductListAPIView.as_view(), name='product_list'),
    path('products/detail/<pk>', ProductDetailAPIView.as_view(), name='product_detail'),
    path('products/delete/<pk>', ProductDeleteAPIView.as_view(), name='product_delete'),
    path('products/update/<pk>', ProductUpdateAPIView.as_view(), name='product_update'),
    path('products/create/', ProductCreateAPIView.as_view(), name='product_create'),
    
]
