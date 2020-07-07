from django.shortcuts import render
from django.http import HttpResponseNotFound
from . import models


# Create your views here.
def index(request):
    context = {}

    products = models.Product.objects.all()
    if 'active' in request.GET:
       products = products.filter(is_active=True)

    if 'category' in request.GET:
       category = request.GET['category']

       try:
          category_int = int(category)
          products = products.filter(category = category_int)
       except:
          return HttpResponseNotFound('Not Found')

    context['products'] = products
    return render(request, 'mysite/index.html', context)

def about(request):
    return render(request, 'mysite/about.html')

def services(request):
    return render(request, 'mysite/services.html')

def portfolio(request):
    return render(request, 'mysite/portfolio.html')






