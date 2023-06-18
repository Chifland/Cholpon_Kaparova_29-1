from django.shortcuts import render
from posts.models import Product, Category


def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all
        context_data = {
            'products': products
        }
        return render(request, 'products/products.html', context=context_data)


def categories_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        context_data = {
            'categories': categories
        }
        return render(request, 'products/category.html', context=context_data)

