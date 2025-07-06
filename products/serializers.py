from rest_framework import serializers
from .models import Product
from .services import GoldPriceService

class ProductSerializer(serializers.ModelSerializer):
    available_colors = serializers.SerializerMethodField()
    formatted_price = serializers.SerializerMethodField()
    dynamic_price = serializers.SerializerMethodField()
    gold_price_per_gram = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'formatted_price', 'dynamic_price', 'gold_price_per_gram', 'popularity_score', 'weight', 'images', 'available_colors', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def get_available_colors(self, obj):
        return obj.get_available_colors()
    
    def get_formatted_price(self, obj):
        return obj.get_formatted_price()
    
    def get_dynamic_price(self, obj):
        return obj.calculate_dynamic_price()
    
    def get_gold_price_per_gram(self, obj):
        return GoldPriceService.get_gold_price_per_gram()

class ProductListSerializer(serializers.ModelSerializer):
    available_colors = serializers.SerializerMethodField()
    formatted_price = serializers.SerializerMethodField()
    dynamic_price = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'formatted_price', 'dynamic_price', 'popularity_score', 'weight', 'images', 'available_colors']
    
    def get_available_colors(self, obj):
        return obj.get_available_colors()
    
    def get_formatted_price(self, obj):
        return obj.get_formatted_price()
    
    def get_dynamic_price(self, obj):
        return obj.calculate_dynamic_price() 