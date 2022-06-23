# from django.shortcuts import render
# from django.http import HttpResponse
# from store.models import Product, OrderItem, Order, Customer 
# from django.db.models import Q, F, Value, Func, Count
# # from django.db.models.aggregates import  Max, Min, Avg, ExpressionWrapper
# from django.db.models.functions import Concat

# # from storefront.store.models import Order

# def say_hello(request):
#     query_set = Customer.objects.annotate(orders_count=Count('order'))
# #example of 1 st code in easy form using Concat:


#     return render(request, 'there.html', {'name': 'Mosh', 'customers': list(query_set)})