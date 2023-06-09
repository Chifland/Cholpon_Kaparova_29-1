from django.shortcuts import render, redirect
from django.db.models import Q
from posts.models import Product, Category
from posts.forms import ProductCreateForm, CategoriesCreateForm
from posts.constants import PAGINATION_LIMIT



def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        search_text = request.GET.get('search')
        page = int(request.GET.get('page', 1))
        max_page = products.__len__() / PAGINATION_LIMIT

        if search_text:
            """startswith, endswith, contains"""
            products = products.filter(Q(name_of_product__contains=search_text) | Q(description__contains=search_text))

        if round(max_page) < max_page:
            max_page = round(max_page)+1
        else:
            max_page = round(max_page)

        products = products[PAGINATION_LIMIT * (page - 1):PAGINATION_LIMIT * page]



        context_data = {
            'products': products,
            'user': request.user,
            'pages': range(1, max_page+1)
        }
        return render(request, 'products/products.html', context=context_data)


def categories_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        context_data = {
            'categories': categories
        }
        return render(request, 'products/category.html', context=context_data)


def product_detail_view(request, pk):
    if request.method == 'GET':
        try:
            product = Product.objects.get(id=pk)
        except Product.DoesNotExist:
            return render(request, 'products/detail.html')
        context_data = {
            'product': product
        }
        return render(request, 'products/detail.html', context=context_data)


def product_create_view(request):
    if request.user.is_anonymous:
        return redirect('/products/')

    if request.method == 'GET':
        context_data = {
            'form': ProductCreateForm
        }
        return render(request, 'products/create.html', context=context_data)

    if request.method == 'POST':
        data, file = request.POST, request.FILES
        form = ProductCreateForm(data, file)


        if form.is_valid():
            Product.objects.create(
                image_of_product=form.cleaned_data.get('image'),
                name_of_product=form.cleaned_data.get('title'),
                measure_of_product=form.cleaned_data.get('measure'),
                cost_of_product=form.cleaned_data.get('cost'),
                amount_of_product=form.cleaned_data.get('amount'),

            )
            return redirect('/products/')

        return render(request, 'products/create.html', context={
            'form': form
        })


def category_create_view(request):
    if request.method == 'GET':
        context_data = {
            'form': CategoriesCreateForm
        }
        return render(request, 'products/createcategory.html', context=context_data)

    if request.method == 'POST':
        data, file = request.POST, request.FILES
        form = CategoriesCreateForm(data, file)


        if form.is_valid():
            Category.objects.create(
                title=form.cleaned_data.get('title'),

            )
            return redirect('/categories/')

        return render(request, 'products/createcategory.html', context={
            'form': form
        })





