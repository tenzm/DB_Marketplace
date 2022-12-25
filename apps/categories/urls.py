from django.urls import path 
from apps.categories import views
from apps.categories.views import category_detail


urlpatterns = [
    path('category/create', views.create_category, name='category_create'),
    path('category/<str:slug>', category_detail, name = "category_detail"),
]