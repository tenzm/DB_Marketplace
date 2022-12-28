from django.urls import path 
from apps.categories import views
from apps.categories.views import category_detail, category_delete


urlpatterns = [
    path('category/create', views.create_category, name='category_create'),
    path('category/delete/<str:slug>', category_delete, name = "category_detail"),
    path('category/<str:slug>', category_detail, name = "category_detail"),
]