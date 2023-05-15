from rest_framework import serializers

from mainapp.models import(
    Category, Product
)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id', 'category', 'name',
            'description', 'price', 'discount',
            'final_price',
        )

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(read_only=True, many=True)
    class Meta:
        model = Category
        fields = (
            'id', 'name', 'products',
        )

