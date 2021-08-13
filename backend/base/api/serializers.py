from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from base.models import Product, Category, Review
from django.contrib.auth.models import User


class ProductSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='base:product_detail',
        lookup_field='slug'
    )

    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return str(obj.user.username)

    category = serializers.SerializerMethodField()

    def get_category(self, obj):
        return str(obj.category.name)

    class Meta:
        model = Product
        fields = [
            'user',
            'url',
            'slug',
            'name',
            'image',
            'brand',
            'category',
            'description',
            'rating',
            'numReviews',
            'price',
            'countInStock',
            'createdAt',
            '_id'
        ]



class CategorySerializer(serializers.ModelSerializer):
    parent = serializers.SerializerMethodField()
    subcategories = serializers.SerializerMethodField()

    def get_parent(self, obj):
        return str(obj.parent)

    def get_subcategories(self,obj):
        if obj.any_children:
            return CategorySerializer(obj.childrens(), many=True).data

    class Meta:
        model = Category
        fields = [
            '_id',
            'name',
            'url',
            'slug',
            'image',
            'parent',
            'subcategories',
        ]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


# ! USER SERIALIZER
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
            'is_staff',
            'is_superuser',
            'is_active',
            'date_joined',
            'last_login'
            
        ]

class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token)

    class Meta:
        model = User
        fields = fields = [
            'id',
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
            'is_staff',
            'is_superuser',
            'is_active',
            'date_joined',
            'last_login',
            'token'
            
        ]