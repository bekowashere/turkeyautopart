from base.models import Product
from base.api.serializers import ProductSerializer

from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, CreateAPIView, RetrieveUpdateAPIView

from rest_framework.permissions import IsAdminUser
from base.api.permissions import IsSuperuser

from rest_framework.filters import SearchFilter, OrderingFilter

from base.api.paginations import ProductPagination

class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['name']
    # pagination_class = ProductPagination

class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # ! lookup_field varsayılan olarak 'pk' dir.
    lookup_field = 'slug'

class ProductDeleteAPIView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'
    permission_classes = [IsSuperuser]

class ProductUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'
    permission_classes = [IsSuperuser]

class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]
    

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    