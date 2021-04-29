from django.shortcuts import render


def products(request):
    context = {
        'date': 'горячее предложение до '
    }
    return render(request, 'mainapp/products.html', context=context)
