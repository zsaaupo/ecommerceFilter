from django.contrib import admin
from django.urls import path
from .views import ProductList

urlpatterns = [
    path('', ProductList.as_view()),
]
