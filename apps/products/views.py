from django.shortcuts import render, redirect, get_object_or_404
from apps.cart.models import Cart, CartManager
from apps.products.models import Product, ProductComment
from apps.settings.utils import get_basic_context
from apps.settings.models import Setting
from apps.categories.models import Category
from django.db.models import Q
from apps.products.forms import ProductCreateForm, ProductUpdateForm, EmailPostForm
from django.core.mail import send_mail

# Create your views here.
def product_detail(request, slug):
    product = Product.objects.get(slug = slug)
    cart = Cart.objects.filter(user = request.user.id, products = product)
    category = None
    categories = Category.objects.all()
    for c in categories:
        if(c.id == product.category_id):
            category = c
    product.category_id
    if 'like' in request.POST:
        try:
            like = LikeProduct.objects.get(user=request.user, product=product)
            like.delete()
        except:
            LikeProduct.objects.create(user=request.user, product=product)
    if 'comment' in request.POST:
        id = request.POST.get('post_id')
        message = request.POST.get('comment_message')
        comment = ProductComment.objects.create(message=message, product=product, user=request.user)
        return redirect('product_detail', product.slug)

    context = get_basic_context(request)

    context['product']= product
    context['cart']=cart
    context['home']= {}
    context['categories']= categories
    context['current_category']=category
    return render(request, 'products/detail.html', context)

def product_search(request):
    products = Product.objects.all()
    qury_obj = request.GET.get('query')
    if qury_obj:
        products = Product.objects.filter(Q(title__icontains = qury_obj))
    context = get_basic_context(request)
    context["products"] = products
    return render(request, 'products/search.html', context)



def product_create(request):
    form = ProductCreateForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        print(form)
        return redirect('index')

    context = get_basic_context(request)
    context['form']= form
    return render(request, 'products/create.html', context)

def product_update(request, slug):
    product = Product.objects.get(slug = slug)
    form = ProductUpdateForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('product_detail', product.slug)
    context = get_basic_context(request)
    context['form']= form
    return render(request, 'products/update.html', context)

def product_delete(request, slug):
    product = Product.objects.filter(slug = slug).delete()
    return redirect('index')
