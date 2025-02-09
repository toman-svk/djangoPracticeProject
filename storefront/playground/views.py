from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product



def say_hello(request):
    #None
    queryset = Product.objects.filter(title__icontains = 'coffee')

    return render(request, 'hello.html', {'name': 'Filip', 'products': list(queryset)})
