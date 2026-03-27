from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)} # Automatycznie tworzy URL z nazwy

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'is_digital', 'available', 'created_at']
    list_filter = ['available', 'is_digital', 'category']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}