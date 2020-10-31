from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('product_names', 'total_products','total_amount')