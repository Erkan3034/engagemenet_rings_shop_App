from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'popularity_score', 'weight', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['name']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-popularity_score']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'popularity_score', 'weight')
        }),
        ('Images', {
            'fields': ('images',),
            'description': 'JSON format: {"white": "url", "yellow": "url", "rose": "url"}'
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def get_available_colors(self, obj):
        return ', '.join(obj.get_available_colors())
    get_available_colors.short_description = 'Available Colors'
