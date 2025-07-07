from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from products.models import Product
import json

def home(request):
    """Main page view"""
    products = Product.objects.all().order_by('-popularity_score')
    context = {
        'products': products,
        'total_products': products.count(),
    }
    return render(request, 'frontend/home.html', context)

def product_detail(request, product_id):
    """Product detail page view"""
    try:
        product = Product.objects.get(id=product_id)
        # Get other products for related products section
        other_products = Product.objects.exclude(id=product_id).order_by('-popularity_score')[:6]
        context = {
            'product': product,
            'available_colors': product.get_available_colors(),
            'products': other_products,
        }
        return render(request, 'frontend/product_detail.html', context)
    except Product.DoesNotExist:
        return render(request, 'frontend/404.html', status=404)

def products_list(request):
    """Products listing page with filters"""
    products = Product.objects.all()
    
    # Apply filters
    min_popularity = request.GET.get('min_popularity')
    max_popularity = request.GET.get('max_popularity')
    min_weight = request.GET.get('min_weight')
    max_weight = request.GET.get('max_weight')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    search = request.GET.get('search')
    color = request.GET.get('color')
    ordering = request.GET.get('ordering', '-popularity_score')
    
    if min_popularity:
        products = products.filter(popularity_score__gte=float(min_popularity))
    if max_popularity:
        products = products.filter(popularity_score__lte=float(max_popularity))
    if min_weight:
        products = products.filter(weight__gte=float(min_weight))
    if max_weight:
        products = products.filter(weight__lte=float(max_weight))
    if min_price:
        products = products.filter(price__gte=float(min_price))
    if max_price:
        products = products.filter(price__lte=float(max_price))
    if search:
        products = products.filter(name__icontains=search)
    if color:
        products = products.filter(images__has_key=color)
    
    # Apply ordering
    products = products.order_by(ordering)
    
    # Get all available colors for filter
    all_colors = set()
    for product in Product.objects.all():
        all_colors.update(product.get_available_colors())
    
    context = {
        'products': products,
        'total_products': products.count(),
        'available_colors': list(all_colors),
        'color_list': ['yellow', 'white', 'rose'],
        'filters': {
            'min_popularity': min_popularity,
            'max_popularity': max_popularity,
            'min_weight': min_weight,
            'max_weight': max_weight,
            'min_price': min_price,
            'max_price': max_price,
            'search': search,
            'color': color,
            'ordering': ordering,
        }
    }
    return render(request, 'frontend/products_list.html', context)

def api_products(request):
    """API endpoint for products data"""
    products = Product.objects.all()
    data = []
    for product in products:
        data.append({
            'id': product.id,
            'name': product.name,
            'popularity_score': product.popularity_score,
            'weight': product.weight,
            'images': product.images,
            'available_colors': product.get_available_colors(),
        })
    return JsonResponse({'products': data})
