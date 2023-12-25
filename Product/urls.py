from django.urls import path
from .views import ProductList, FilterProduct

urlpatterns = [
    path('', ProductList.as_view()),
    path('filter/', FilterProduct.as_view()),
]
