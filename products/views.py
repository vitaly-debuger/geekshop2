import json

from django.shortcuts import render
from django.conf import settings
from products.models import Product, ProductCategory


# Функции = контроллеры = вьюхи

def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'products/index.html', context)


def products(request):
    file_path = settings.BASE_DIR / 'products/fixtures/goods.json'
    context = {
        'title': 'GeekShop - Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context=context)
