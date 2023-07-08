from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.generic import ListView, CreateView
from posts.models import Product, Category
from posts.forms import ProductCreateForm, CategoriesCreateForm
from posts.constants import PAGINATION_LIMIT


class MainPageCBV(ListView):
    model = Product
    template_name = 'layouts/index.html'


class ProductsCBV(ListView):
    model = Product
    template_name = 'products/products.html'

    def get(self, request, *args, **kwargs):
        products = self.model.objects.all()
        search_text = request.GET.get('search')
        page = int(request.GET.get('page', 1))
        max_page = products.__len__() / PAGINATION_LIMIT

        if search_text:
            """startswith, endswith, contains"""
            products = products.filter(Q(name_of_product__contains=search_text) | Q(description__contains=search_text))

        if round(max_page) < max_page:
            max_page = round(max_page) + 1
        else:
            max_page = round(max_page)

        products = products[PAGINATION_LIMIT * (page - 1):PAGINATION_LIMIT * page]

        context_data = {
            'products': products,
            'user': request.user,
            'pages': range(1, max_page + 1)
        }
        return render(request, self.template_name, context=context_data)


class CategoriesCBV(ListView):
    model = Category
    template_name = 'products/category.html'

    def get(self, request, *args, **kwargs):
        categories = self.model.objects.all()
        context_data = {
            'categories': categories
        }
        return render(request, self.template_name, context=context_data)


class ProductDetailCBV(ListView):
    model = Product
    template_name = 'products/detail.html'

    def get(self, request, pk, *args, **kwargs,):
        try:
            product = self.model.objects.get(id=pk)
        except Product.DoesNotExist:
            return render(request, 'products/detail.html')
        context_data = {
            'product': product
        }
        return render(request, self.template_name, context=context_data)



# def product_create_view(request):
#     if request.user.is_anonymous:
#         return redirect('/products/')
#
#     if request.method == 'GET':
#         context_data = {
#             'form': ProductCreateForm
#         }
#         return render(request, 'products/create.html', context=context_data)
#
#     if request.method == 'POST':
#         data, file = request.POST, request.FILES
#         form = ProductCreateForm(data, file)
#
#
#         if form.is_valid():
#             Product.objects.create(
#                 image_of_product=form.cleaned_data.get('image'),
#                 name_of_product=form.cleaned_data.get('title'),
#                 measure_of_product=form.cleaned_data.get('measure'),
#                 cost_of_product=form.cleaned_data.get('cost'),
#                 amount_of_product=form.cleaned_data.get('amount'),
#
#             )
#             return redirect('/products/')
#
#         return render(request, 'products/create.html', context={
#             'form': form
#         })
class ProductCreateCBV(ListView,CreateView):
    model = Product
    template_name = 'products/create.html'


    def get(self, request, *args, **kwargs,):
        if request.user.is_anonymous:
            return redirect('/products/')
        else:
            context_data = {
                'form': ProductCreateForm
            }
            return render(request, self.template_name, context=context_data)

    def post(self, request, *args, **kwargs):
        data, file = request.POST, request.FILES
        form = ProductCreateForm(data, file)

        if form.is_valid():
            self.model.objects.create(
                image_of_product=form.cleaned_data.get('image'),
                name_of_product=form.cleaned_data.get('title'),
                measure_of_product=form.cleaned_data.get('measure'),
                cost_of_product=form.cleaned_data.get('cost'),
                amount_of_product=form.cleaned_data.get('amount'),
                description=form.cleaned_data.get('description'),

            )
            return redirect('/products/')

        return render(request, self.template_name, context={
            'form': form
        })


class CategoryCreateCBV(ListView, CreateView):
    model = Category
    template_name = 'products/createcategory.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return redirect('/categories/')
        else:
            context_data = {
                'form': CategoriesCreateForm
            }
            return render(request, self.template_name, context=context_data)

    def post(self, request, *args, **kwargs):
        data, file = request.POST, request.FILES
        form = CategoriesCreateForm(data, file)

        if form.is_valid():
            self.model.objects.create(
                title=form.cleaned_data.get('title'),

            )
            return redirect('/categories/')

        return render(request, self.template_name, context={
            'form': form
        })






