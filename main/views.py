from django.shortcuts import render
from .models import Products

def home(request):
    return render(request, 'main/home.html')  # Assurez-vous d'avoir un template 'home.html'

def products_list(request) :
    products = Products.objects.all()
    return render(request,'main/products_list.html',{'products': products})

