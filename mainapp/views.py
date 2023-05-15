from rest_framework.viewsets import ModelViewSet

from mainapp.models import Category, Product

from mainapp.serializers import(
    ProductSerializer,
    CategorySerializer,
)

from rest_framework.decorators import action
from rest_framework.response import Response

class CategoryView(ModelViewSet):
    queryset = Category.objects.all()                   
    serializer_class = CategorySerializer

class ProductView(ModelViewSet):
    queryset = Product.objects.all()                   
    serializer_class = ProductSerializer

    @action(methods=['get', ], detail=False)
    def get_discount_product(self, request, *args, **kwargs):
        products = Product.objects.filter(discount__gt=0)
        serializers = ProductSerializer(products, many=True).data
        return Response(serializers)