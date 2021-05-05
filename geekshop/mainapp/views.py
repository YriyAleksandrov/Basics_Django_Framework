from django.shortcuts import render
from .models import ProductCategory


def products(request):

    products_category = ProductCategory.objects.all()[:5]

    links_menu = {'links': [
        {'href': 'products', 'name': products_category},
        {'href': 'products', 'name': products_category},
        {'href': 'products', 'name': products_category},
        {'href': 'products', 'name': products_category},
        {'href': 'products', 'name': products_category},
    ]}

    return render(request, 'mainapp/products.html', context=links_menu)

