from django.contrib import admin
from .models import Product, Review, Order, OrderItem, ShippingAddress
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'category',
                    'rating', 'price', 'countInStock')
    list_display_links = ('name',)
    list_editable = ('brand', 'category', 'price')
    search_fields = ('name', 'brand', 'category')
    list_filter = ('brand', 'category')
    prepopulated_fields = {'slug': ('brand','name',)}

    class Meta:
        model = Product


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'name', 'rating')
    list_display_links = ('product',)
    list_editable = ('rating',)
    search_fields = ('product', 'user')

    class Meta:
        model = Review


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'paymentMethod', 'totalPrice',
                    'isPaid', 'isDelivered', 'createdAt')
    list_display_links = ('user',)
    list_editable = ('isPaid', 'isDelivered')
    search_fields = ('user', 'paymentMethod')
    list_filter = ('paymentMethod', 'isPaid', 'isDelivered')

    class Meta:
        model = Order


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'name', 'qty', 'price')
    list_display_links = ('name',)
    search_fields = ('order', 'product', 'name')

    class Meta:
        model = OrderItem


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('address','order', 'country', 'city', 'shippingPrice')
    list_display_links = ('address',)
    search_fields = ('country', 'city')
    list_filter = ('country',)

    class Meta:
        model = ShippingAddress
