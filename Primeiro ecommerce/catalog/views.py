from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Product,Category

def product_list(request):
    context = {
        "product_list":Product.objects.all()
    }
    return render(request,"catalog/product_list.html",context)

def category(request,category_slug):
    category=Category.objects.get(slug=category_slug)
    context = {
        "current_category" : category,
        "product_list":Product.objects.filter(category=category)
    }
    return render(request,"catalog/category.html",context)