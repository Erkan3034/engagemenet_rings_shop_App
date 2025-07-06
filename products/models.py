from django.db import models
from decimal import Decimal
from .services import PriceCalculator
import json

class Product(models.Model):
    name = models.CharField(max_length=200)
    popularity_score = models.FloatField(default=0.0)
    weight = models.FloatField(default=0.0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    images = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-popularity_score']

    def __str__(self):
        return self.name

    def get_image_url(self, color):
        """Get image URL for specific color"""
        return self.images.get(color, '')

    def get_available_colors(self):
        """Get list of available colors"""
        return list(self.images.keys())

    def calculate_dynamic_price(self):
        """Calculate price using formula: (popularityScore + 1) * weight * goldPrice"""
        return PriceCalculator.calculate_price(self.popularity_score, self.weight)

    def get_formatted_price(self):
        """Get formatted price with currency"""
        dynamic_price = self.calculate_dynamic_price()
        return f"${dynamic_price:,.2f} USD"

    def get_static_formatted_price(self):
        """Get formatted static price (for comparison)"""
        return f"${self.price:,.2f} USD"

    def save(self, *args, **kwargs):
        """Override save to calculate dynamic price"""
        # Calculate and update the static price field
        self.price = self.calculate_dynamic_price()
        super().save(*args, **kwargs)

    def get_popularity_score_out_of_5(self):
        """Get popularity score out of 5 with 1 decimal place"""
        return round(self.popularity_score * 5, 1)
    
    def get_filled_stars_count(self):
        """Get number of filled stars (integer)"""
        return int(self.popularity_score * 5)
    
    def get_empty_stars_count(self):
        """Get number of empty stars"""
        return 5 - self.get_filled_stars_count()
