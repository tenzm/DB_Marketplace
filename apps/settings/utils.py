import sys
from django.shortcuts import render
from apps.settings.models import Setting, About, Team
from apps.products.models import Product, ProductComment
from apps.categories.models import Category
from django.template import RequestContext
from apps.cart.models import Cart, CartManager


def get_basic_context(request):
    home = {}
    slide_products = Product.objects.all().order_by('-id')
    products = Product.objects.all().order_by('-id')

    cart_len = Cart.objects.filter(user = request.user.id).count()

    categories = Category.objects.all().order_by('-id')
    categories_dict = {}
    for c in categories:
        categories_dict[c.id] = c.title
    
    
    products_list = []

    for p in products:
        products_list.append(
            {
                "id": p.id,
                "title": p.title,
                "price": p.price,
                "description": p.description,
                "main_product_image": p.main_product_image,
                "category": categories_dict[p.category_id],
                "slug": p.slug

            }
        )

    most_popular_product = Product.objects.all().order_by('-price')
    comments = ProductComment.objects.all().order_by('-id')
    context = {
        'home' : home,
        'products' : products_list,
        'slide_products' : slide_products,
        'categories' : categories,
        'most_popular_product' : most_popular_product,
        'comments' : comments,
        "cart_len": cart_len
    }
    return context