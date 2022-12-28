from django.shortcuts import render, redirect, get_object_or_404
from apps.settings.utils import get_basic_context
from apps.categories.forms import CategoryCreateForm
from apps.categories.models import Category
from apps.products.models import Product
from apps.settings.models import Setting
from django.core.paginator import Paginator

# Create your views here.
def category_detail(request, slug):
    category = Category.objects.get(slug = slug)
    categories = Category.objects.all().order_by('?')[:5]
    products = Product.objects.all().order_by('-id')
    paginator = Paginator(products, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'category' : category,
        'products' : products,
        'home' : {},
        'categories' : categories,
        'page_obj': page_obj,
    }
    return render(request, 'category_detail.html', context)

def create_category(request):
    form = CategoryCreateForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('index')

    context = get_basic_context(request)

    context['form'] = form
    

    return render(request, 'category/create.html', context)