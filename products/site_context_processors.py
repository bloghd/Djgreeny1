from .models import Category, Brand, Product

def get_category(request):
    categories = Category.objects.all()
    brands = Brand.objects.all()
    return {'categories':categories, 'brands':brands}