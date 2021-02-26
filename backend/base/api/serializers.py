from rest_framework import serializers
from base.models import Product

class ProductSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()
    def get_user(self,obj):
        return str(obj.user.username)

    class Meta:
        model = Product
        fields = [
            'user',
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
    