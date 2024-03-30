from django.shortcuts import render


def index(request):
    context = {
        'title': 'Test title',
        'username': 'Alex',
    }
    return render(request, 'products/index.html')


def products(request):
    return render(request, 'products/products.html')
