from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, ProductImages, Review, Category, Brand
from django.db.models import Count

# Create your views here.

class ProductListView(ListView):
    model = Product
    paginate_by = 1
    template_name = 'product_list.html'

class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        myproduct = self.get_object()
        context["images"] = ProductImages.objects.filter(product=myproduct)
        context["reviews"] = Review.objects.filter(product=myproduct)
        return context
    
class CategoryListView(ListView):
    model = Category
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all().annotate(product_count=Count('product_category'))
        return context

class BrandListView(ListView):
    model = Brand
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = Brand.objects.all().annotate(product_count=Count('product_brand'))
        return context


class BrandDetailView(DetailView):
    model = Brand
    
    


    
    


