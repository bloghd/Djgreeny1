from django.contrib import admin
from .models import Product, ProductImages, Category, Brand, Review
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
class ProductImagesInLine(admin.TabularInline):
    model = ProductImages

class ProductAdmin(SummernoteModelAdmin):
    inlines = [ProductImagesInLine]
    summernote_fields = '__all__'

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Review)
admin.site.register(ProductImages)
    