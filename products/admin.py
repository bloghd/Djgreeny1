from django.contrib import admin
from .models import Product, ProductImages, Category, Brand, Review
# Register your models here.
class ProductImagesInLine(admin.TabularInline):
    model = ProductImages

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesInLine]

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Review)
admin.site.register(ProductImages)
    