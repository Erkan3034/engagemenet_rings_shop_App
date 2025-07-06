from django.db import models
import json

class Product(models.Model):
    name = models.CharField(max_length=200)
    popularity_score = models.FloatField(default=0.0)
    weight = models.FloatField(default=0.0)
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
