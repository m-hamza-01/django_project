from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count, Max
from store.models import Product, OrderItem

# Create your views here.

def say_hello(request):

    # queryset = Product.objects.values('id','title','collection__title').order_by('title')[0:10]
    # queryset = Product.objects.filter(unit_price__range=(100, 200))

    # queryset = Product.objects.filter(id__in=OrderItem.objects.values('product__id').distinct()).order_by('title')
    # queryset = OrderItem.objects.values('product__id').distinct()

    queryset = Product.objects.prefetch_related('promotions').all()
    
    return render(request, 'bye.html',{'name':'Hamza','products':list(queryset)})