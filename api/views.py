from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product

# Create your views here.

def say_hello(request):

    queryset = Product.objects.values('id','title','collection__title').order_by('title')[0:10]


    
    return render(request, 'hello.html',{'name':'Hamza','products':list(queryset)})