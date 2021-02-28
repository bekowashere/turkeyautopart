from django.urls import path, include

from base.api.views import ProductListAPIView, ProductDetailAPIView, ProductDeleteAPIView, ProductUpdateAPIView, ProductCreateAPIView

app_name = 'base'


urlpatterns = [
    path('products', ProductListAPIView.as_view(), name='product_list'),
    path('products/detail/<slug>', ProductDetailAPIView.as_view(), name='product_detail'),
    path('products/delete/<slug>', ProductDeleteAPIView.as_view(), name='product_delete'),
    path('products/update/<slug>', ProductUpdateAPIView.as_view(), name='product_update'),
    path('products/create/', ProductCreateAPIView.as_view(), name='product_create'),
    
]
