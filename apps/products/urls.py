from django.urls import path 
from apps.products.views import product_delete, product_detail, product_search, product_create, product_update


urlpatterns = [
    path('product/<str:slug>', product_detail, name = "product_detail"),
    path('search/', product_search, name = "product_search"),
    path('create/', product_create, name = "product_create"),
    path('update/<str:slug>', product_update, name = "product_update"),
    path('delete/<str:slug>', product_delete, name = "product_delete")
]