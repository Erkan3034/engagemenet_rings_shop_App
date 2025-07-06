import json
import os
from django.core.management.base import BaseCommand
from products.models import Product
from decimal import Decimal

class Command(BaseCommand):
    help = 'Load engagement rings from JSON file'

    def handle(self, *args, **options):
        # Clear existing products
        Product.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Cleared existing products'))

        # Get the JSON file path
        json_file = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), 'products.json')
        
        try:
            with open(json_file, 'r', encoding='utf-8') as file:
                products_data = json.load(file)
                
            self.stdout.write(f'Found {len(products_data)} products in JSON file')
            
            for product_data in products_data:
                try:
                    # Create the product using the CDN image URLs directly
                    product = Product.objects.create(
                        name=product_data['name'],
                        weight=Decimal(str(product_data['weight'])),
                        popularity_score=Decimal(str(product_data['popularityScore'])),
                        images={
                            'yellow': product_data['images']['yellow'],
                            'white': product_data['images']['white'],
                            'rose': product_data['images']['rose']
                        }
                    )
                    
                    self.stdout.write(f'Created product: {product.name} - Price: ${product.get_dynamic_price():.2f}')
                    
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(f'Error creating product {product_data.get("name", "Unknown")}: {str(e)}')
                    )
                    continue
                    
            self.stdout.write(
                self.style.SUCCESS(f'Successfully loaded {Product.objects.count()} products')
            )
            
        except FileNotFoundError:
            self.stdout.write(
                self.style.ERROR(f'JSON file not found: {json_file}')
            )
        except json.JSONDecodeError as e:
            self.stdout.write(
                self.style.ERROR(f'Error parsing JSON file: {str(e)}')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Unexpected error: {str(e)}')
            ) 