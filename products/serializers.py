from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    available_colors = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'popularity_score', 'weight', 'images', 'available_colors', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def get_available_colors(self, obj):
        return obj.get_available_colors()

class ProductListSerializer(serializers.ModelSerializer):
    available_colors = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'popularity_score', 'weight', 'images', 'available_colors']
    
    def get_available_colors(self, obj):
        return obj.get_available_colors() 