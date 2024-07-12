from django.urls import path
from .views import ProductListView, ProductDetailView, CategoryListView, BrandListView

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('brand/', BrandListView.as_view(), name='brand_list'),
    path('<slug:slug>', ProductDetailView.as_view(), name='product_detail'),
]
