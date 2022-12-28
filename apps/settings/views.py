from django.shortcuts import render
from apps.settings.models import Setting, About, Team
from apps.settings.utils import  get_basic_context
from apps.products.models import Product, ProductComment
from apps.categories.models import Category
from django.template import RequestContext

# Create your views here.
def index(request):
    context = get_basic_context(request)
    return render(request, 'index-2.html', context)

def about_us(request):
    home = Setting.objects.latest('id')
    about = About.objects.latest('id')
    teams = Team.objects.all().order_by('-id')
    context = {
        'home' : home,
        'about' : about,
        'teams' : teams
    }
    return render(request, 'about.html',context)

def handler404(request, exception):
    home = Setting.objects.latest('id')
    categories = Category.objects.all().order_by('-id')
    context = {
        'home' : home,
        'categories' : categories,
    }
    response = render(request, "404.html", context=context)
    response.status_code = 404
    return response