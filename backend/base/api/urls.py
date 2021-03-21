from django.urls import path, include

from base.api.views import (
    ProductListAPIView,
    ProductDetailAPIView,
    ProductDeleteAPIView,
    ProductUpdateAPIView,
    ProductCreateAPIView,
    CategoryListAPIView,
    CategoryDetailAPIView,
    CategoryDeleteAPIView,
    CategoryUpdateAPIView,
    CategoryCreateAPIView,
    ReviewListAPIView,
    ReviewDeleteAPIView,
    ReviewUpdateAPIView,
    ReviewCreateAPIView,
    MyTokenObtainPairView,
    UserListAPIView,
    UserDetailAPIView
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'base'


urlpatterns = [
    path('products', ProductListAPIView.as_view(), name='product_list'),
    path('products/detail/<slug>', ProductDetailAPIView.as_view(), name='product_detail'),
    path('products/delete/<slug>', ProductDeleteAPIView.as_view(), name='product_delete'),
    path('products/update/<slug>', ProductUpdateAPIView.as_view(), name='product_update'),
    path('products/create/', ProductCreateAPIView.as_view(), name='product_create'),

    path('categories', CategoryListAPIView.as_view(), name='category_list'),
    path('categories/detail/<slug>', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('categories/delete/<slug>', CategoryDeleteAPIView.as_view(), name='category_delete'),
    path('categories/update/<slug>', CategoryUpdateAPIView.as_view(), name='category_update'),
    path('categories/create/', CategoryCreateAPIView.as_view(), name='category_create'),

    path('comments', ReviewListAPIView.as_view(), name='comment_list'),
    path('comments/delete/<pk>', ReviewDeleteAPIView.as_view(), name='comment_delete'),
    path('comments/update/<pk>', ReviewUpdateAPIView.as_view(), name='comment_update'),
    path('comments/create/', ReviewCreateAPIView.as_view(), name='comment_create'),

    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('users', UserListAPIView.as_view(), name='user_list'),
    path('users/<pk>', UserDetailAPIView.as_view(), name='user_detail'),
    
]
