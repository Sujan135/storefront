from cgitb import reset
from turtle import title
from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product, OrderItem, Order, Customer, Collection
# from storefront.store.models import Collection
from tags.models import TaggedItem
from django.db import transaction


def say_hello(request):

#....

    with transaction.atomic():
        order = Order()
        order.customer_id = 1 
        order.save()

        item = OrderItem()
        item.order = order
        item.product_id = 1
        item.quantity = 1
        item.unit_price = 10
        item.save()
        

    return render(request, 'there.html',{'name': 'Mosh',})




   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    #  def say_hello(request):
    # query_set = Customer.objects.annotate(full_name=Func(F('first_name'), Value(' '), F('last_name'), function='CONCAT'))
#example of 1 st code in easy form using Concat:
    # query_set = Customer.objects.annotate(full_name=Concat('first_name', Value(' '), 'last_name'))