from decimal import Decimal

from django.db.models import query
from .models import Product, Collection
from rest_framework import serializers

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']

    products_count = serializers.IntegerField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'slug', 'inventory', 'price', 'price_with_tax', 'collection']

    price = serializers.DecimalField(max_digits=10, decimal_places=2, source='unit_price')
    price_with_tax = serializers.SerializerMethodField(method_name="calculate_tax")
    collection = serializers.HyperlinkedRelatedField(
        queryset=Collection.objects.all(),
        view_name='collection-detail'
    )

    def calculate_tax(self, product: Product):
        tax = product.unit_price * Decimal(0.1)  # Assuming a 10% tax rate
        return product.unit_price + tax
