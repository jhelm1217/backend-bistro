from rest_framework import serializers
from .models import *

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'cuisine', 'title', 'category', 'description', 'price']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name']

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
        model = Driver
        fields = ['id', 'name', 'phone_number', 'vehicle_make', 'license_plate_number']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'customer', 'driver', 'rating', 'comment', 'created_at']
        