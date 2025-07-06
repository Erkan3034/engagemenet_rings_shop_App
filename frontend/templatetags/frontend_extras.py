from django import template
register = template.Library()

@register.filter
def dict_get(d, key): 
    return d.get(key, '') 

@register.filter
def mul(value, arg):
    """Çarpma filtresi: value * arg"""
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return '' 

@register.filter
def subtract(value, arg):
    """Çıkarma filtresi: value - arg"""
    try:
        return float(value) - float(arg)
    except (ValueError, TypeError):
        return '' 