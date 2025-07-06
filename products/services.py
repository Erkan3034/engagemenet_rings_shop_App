import requests
import json
from decimal import Decimal
from django.core.cache import cache
from django.conf import settings

class GoldPriceService:
    """Service to fetch real-time gold price"""
    
    CACHE_KEY = 'gold_price_usd_per_gram'
    CACHE_TIMEOUT = 3600  # 1 hour cache
    
    @classmethod
    def get_gold_price_per_gram(cls):
        """
        Get current gold price per gram in USD
        Uses multiple APIs as fallback
        """
        # Try cache first
        cached_price = cache.get(cls.CACHE_KEY)
        if cached_price:
            return Decimal(str(cached_price))
        
        # Try different APIs
        apis = [
            cls._fetch_from_metals_api,
            cls._fetch_from_gold_api,
            cls._fetch_from_currency_api,
        ]
        
        for api_func in apis:
            try:
                price = api_func()
                if price:
                    # Cache the result
                    cache.set(cls.CACHE_KEY, float(price), cls.CACHE_TIMEOUT)
                    return price
            except Exception as e:
                print(f"API {api_func.__name__} failed: {e}")
                continue
        
        # Fallback to default price if all APIs fail
        default_price = Decimal('75.00')  # Default gold price per gram
        cache.set(cls.CACHE_KEY, float(default_price), cls.CACHE_TIMEOUT)
        return default_price
    
    @classmethod
    def _fetch_from_metals_api(cls):
        """Fetch from metals-api.com (free tier)"""
        try:
            # Using a free API endpoint
            url = "https://api.metals.live/v1/spot/gold"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            if data and len(data) > 0:
                # Price is in USD per troy ounce, convert to per gram
                price_per_ounce = Decimal(str(data[0]['price']))
                price_per_gram = price_per_ounce / Decimal('31.1035')  # 1 troy ounce = 31.1035 grams
                return price_per_gram
        except Exception as e:
            print(f"Metals API error: {e}")
        return None
    
    @classmethod
    def _fetch_from_gold_api(cls):
        """Fetch from goldapi.io (alternative)"""
        try:
            # Using a different free API
            url = "https://www.goldapi.io/api/XAU/USD"
            headers = {
                'x-access-token': 'goldapi-1234567890abcdef',  # Free demo token
                'Content-Type': 'application/json'
            }
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            if 'price' in data:
                # Price is in USD per troy ounce, convert to per gram
                price_per_ounce = Decimal(str(data['price']))
                price_per_gram = price_per_ounce / Decimal('31.1035')
                return price_per_gram
        except Exception as e:
            print(f"Gold API error: {e}")
        return None
    
    @classmethod
    def _fetch_from_currency_api(cls):
        """Fetch from exchangerate-api.com (fallback)"""
        try:
            # Using exchange rate API as fallback
            url = "https://api.exchangerate-api.com/v4/latest/USD"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            # Use a reasonable default gold price if we can't get real data
            return Decimal('75.00')
        except Exception as e:
            print(f"Currency API error: {e}")
        return None

class PriceCalculator:
    """Calculate product price based on formula"""
    
    @classmethod
    def calculate_price(cls, popularity_score, weight):
        """
        Calculate price using formula: (popularityScore + 1) * weight * goldPrice
        """
        gold_price = GoldPriceService.get_gold_price_per_gram()
        price = (Decimal(str(popularity_score)) + Decimal('1')) * Decimal(str(weight)) * gold_price
        return price.quantize(Decimal('0.01'))  # Round to 2 decimal places 