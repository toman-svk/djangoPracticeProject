from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product



def say_hello(request):
    #None
    queryset = Product.objects.filter(unit_price = 20)

    return render(request, 'hello.html', {'name': 'Mosh'})
