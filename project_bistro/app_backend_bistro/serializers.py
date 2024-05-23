from rest_framework import serializers
from .models import *

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'cuisine', 'title', 'category', 'price']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = []

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'customer_name', 'item', 'status', 'created_at']

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'menu_item', 'quantity']

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = []


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = []
        