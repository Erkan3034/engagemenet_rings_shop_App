from django.core.management.base import BaseCommand
from products.models import Product
import json
import os

class Command(BaseCommand):
    help = 'Load products from JSON file'

    def handle(self, *args, **options):
        # Path to the products.json file (relative to project root)
        json_file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), 'products.json')
        
        try:
            with open(json_file_path, 'r', encoding='utf-8') as file:
                products_data = json.load(file)
            
            created_count = 0
            updated_count = 0
            
            for product_data in products_data:
                # Check if product already exists
                product, created = Product.objects.get_or_create(
                    name=product_data['name'],
                    defaults={
                        'popularity_score': product_data['popularityScore'],
                        'weight': product_data['weight'],
                        'images': product_data['images']
                    }
                )
                
                if created:
                    created_count += 1
                    self.stdout.write(
                        self.style.SUCCESS(f'Created product: {product.name}')
                    )
                else:
                    # Update existing product
                    product.popularity_score = product_data['popularityScore']
                    product.weight = product_data['weight']
                    product.images = product_data['images']
                    product.save()
                    updated_count += 1
                    self.stdout.write(
                        self.style.WARNING(f'Updated product: {product.name}')
                    )
            
            self.stdout.write(
                self.style.SUCCESS(
                    f'Successfully loaded products. Created: {created_count}, Updated: {updated_count}'
                )
            )
            
        except FileNotFoundError:
            self.stdout.write(
                self.style.ERROR(f'Products JSON file not found at: {json_file_path}')
            )
        except json.JSONDecodeError as e:
            self.stdout.write(
                self.style.ERROR(f'Invalid JSON format: {e}')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error loading products: {e}')
            ) 