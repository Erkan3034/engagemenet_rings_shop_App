from django.db import models
from decimal import Decimal
import json

class Product(models.Model):
    name = models.CharField(max_length=200)
    popularity_score = models.DecimalField(max_digits=3, decimal_places=2)  # 0.00 to 1.00
    weight = models.DecimalField(max_digits=5, decimal_places=2)  # in grams
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
        """Return list of available colors for this product"""
        return list(self.images.keys()) if self.images else []

    def get_dynamic_price(self):
        """Calculate dynamic price based on current gold price"""
        # Simple formula: (popularity_score + 1) * weight * base_gold_price
        base_gold_price = Decimal('65.00')  # Base gold price per gram
        # Convert popularity_score to Decimal for calculation
        popularity_decimal = Decimal(str(self.popularity_score))
        return (popularity_decimal + Decimal('1')) * self.weight * base_gold_price

    def get_formatted_price(self):
        """Get formatted price string"""
        price = self.get_dynamic_price()
        return f"${price:.2f}"

    def get_static_formatted_price(self):
        """Get formatted static price (for comparison)"""
        return f"${self.price:,.2f} USD"

    def save(self, *args, **kwargs):
        """Override save to calculate dynamic price"""
        # Calculate and update the static price field
        self.price = self.get_dynamic_price()
        super().save(*args, **kwargs)

    def get_popularity_score_out_of_5(self):
        """Convert popularity score to 5-point scale"""
        return float(self.popularity_score) * 5

    def get_filled_stars_count(self):
        """Get number of filled stars for display"""
        score_out_of_5 = self.get_popularity_score_out_of_5()
        return int(score_out_of_5)

    def get_empty_stars_count(self):
        """Get number of empty stars"""
        return 5 - self.get_filled_stars_count()


