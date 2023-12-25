from django.contrib import admin
from .models import Product

# class ProductAdmin(admin.ModelAdmin):
    
#     fields = [
#         "name",
#         "price",
#         "categories",
#         "selected_option",
#         "available_bands"
#     ]
    
#     list_display = [
#         "name",
#         "price",
#     ]
    
#     def available_bands(self, obj):
#         return ", ".join([option.option_name for option in obj.available_bands.all()])
#     available_bands.short_description = 'Available Bands'
    
admin.site.register(Product)