import sys
from django.shortcuts import render
from apps.settings.models import Setting, About, Team
from apps.products.models import Product, Discount, ProductComment
from apps.categories.models import Category
from django.template import RequestContext
from apps.cart.models import Cart, CartManager


def get_basic_context(request):
    home = {}
    slide_products = Product.objects.all().order_by('-id')[:5]
    products = Product.objects.all().order_by('-id')[:8]
    one_random_product = Product.objects.all().order_by('?')[:1]
    two_random_product = Product.objects.all().order_by('?')[:1]
    three_random_product = Product.objects.all().order_by('?')[:1]

    cart_len = Cart.objects.filter(user = request.user.id).count()

    expensive_products = Product.objects.all().order_by('-price')[:3]
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

    discount_product = Discount.objects.all()[:1]
    most_popular_product = Product.objects.all().order_by('-price')
    comments = ProductComment.objects.all().order_by('-id')
    context = {
        'home' : home,
        'products' : products_list,
        'slide_products' : slide_products,
        'one_random_product' : one_random_product,
        'two_random_product' : two_random_product,
        'three_random_product' : three_random_product,
        'expensive_products' : expensive_products,
        'categories' : categories,
        'discount_product' : discount_product,
        'most_popular_product' : most_popular_product,
        'comments' : comments,
        "cart_len": cart_len
    }
    return context