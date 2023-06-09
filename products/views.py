from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def index(request):
    # get all the products from our database.
    products = Product.objects.all()
    return render(request, 'index.html',
                  {'products': products})


def new(request):
    return HttpResponse('New Products')

