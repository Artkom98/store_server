from django.shortcuts import render
from products.models import ProductCategory, Product
from users.models import User, AbstractUser


def index(request):
    context = {
        'title': 'Store',
        'users': User.objects.all(),
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Store - catalog',
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.all(),
    }
    return render(request, 'products/products.html', context)
