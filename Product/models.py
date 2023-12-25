from django.db import models
from filter.models import Category, Option


class Product(models.Model):
    
    name = models.CharField(max_length=255)
    price = models.FloatField()
    categories = models.ManyToManyField(Category, related_name="products")
    # selected_option = models.ForeignKey(Option, null=True, blank=True, on_delete=models.SET_NULL, related_name="selected_products")
    
    @property
    def available_bands(self):
        # Fetch options based on the categories associated with the product
        category_names = self.categories.values_list('category_name', flat=True)
        available_options = Option.objects.filter(categories__category_name__in=category_names).distinct()
        return available_options
    
    def __str__(self) -> str:
        return self.name