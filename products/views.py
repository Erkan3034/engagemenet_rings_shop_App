from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters import rest_framework as filters
from .models import Product
from .serializers import ProductSerializer, ProductListSerializer
from .services import GoldPriceService, PriceCalculator

# Create your views here.

class ProductFilter(filters.FilterSet):
    min_popularity = filters.NumberFilter(field_name="popularity_score", lookup_expr='gte')
    max_popularity = filters.NumberFilter(field_name="popularity_score", lookup_expr='lte')
    min_weight = filters.NumberFilter(field_name="weight", lookup_expr='gte')
    max_weight = filters.NumberFilter(field_name="weight", lookup_expr='lte')
    name = filters.CharFilter(lookup_expr='icontains')
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    
    class Meta:
        model = Product
        fields = ['name', 'popularity_score', 'weight', 'price']

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    search_fields = ['name']
    ordering_fields = ['name', 'popularity_score', 'weight', 'created_at']
    ordering = ['-popularity_score']

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        return ProductSerializer

    @action(detail=False, methods=['get'])
    def popular(self, request):
        """Get products with high popularity score"""
        popular_products = self.queryset.filter(popularity_score__gte=0.8)
        serializer = self.get_serializer(popular_products, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def colors(self, request):
        """Get all available colors across all products"""
        all_colors = set()
        for product in self.queryset:
            all_colors.update(product.get_available_colors())
        return Response({'colors': list(all_colors)})

    @action(detail=True, methods=['get'])
    def images(self, request, pk=None):
        """Get all images for a specific product"""
        product = self.get_object()
        return Response({
            'product_name': product.name,
            'images': product.images
        })

    @action(detail=False, methods=['get'])
    def gold_price(self, request):
        """Get current gold price per gram"""
        try:
            gold_price = GoldPriceService.get_gold_price_per_gram()
            return Response({
                'gold_price_per_gram_usd': float(gold_price),
                'formatted_price': f"${gold_price:,.2f} USD per gram",
                'cache_info': 'Price is cached for 1 hour'
            })
        except Exception as e:
            return Response({
                'error': 'Failed to fetch gold price',
                'message': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['get'])
    def price_formula(self, request):
        """Get price calculation formula and example"""
        try:
            # Example calculation
            example_popularity = 0.85
            example_weight = 2.1
            example_price = PriceCalculator.calculate_price(example_popularity, example_weight)
            gold_price = GoldPriceService.get_gold_price_per_gram()
            
            return Response({
                'formula': '(popularityScore + 1) * weight * goldPrice',
                'example': {
                    'popularity_score': example_popularity,
                    'weight_grams': example_weight,
                    'gold_price_per_gram': float(gold_price),
                    'calculation': f"({example_popularity} + 1) * {example_weight} * {float(gold_price)}",
                    'result': float(example_price)
                },
                'current_gold_price': float(gold_price)
            })
        except Exception as e:
            return Response({
                'error': 'Failed to calculate example price',
                'message': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
