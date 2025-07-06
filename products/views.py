from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters import rest_framework as filters
from .models import Product
from .serializers import ProductSerializer, ProductListSerializer

# Create your views here.

class ProductFilter(filters.FilterSet):
    min_popularity = filters.NumberFilter(field_name="popularity_score", lookup_expr='gte')
    max_popularity = filters.NumberFilter(field_name="popularity_score", lookup_expr='lte')
    min_weight = filters.NumberFilter(field_name="weight", lookup_expr='gte')
    max_weight = filters.NumberFilter(field_name="weight", lookup_expr='lte')
    name = filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Product
        fields = ['name', 'popularity_score', 'weight']

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
