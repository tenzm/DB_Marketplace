from django.contrib import admin
from apps.products.models import Product, ProductComment

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    inlines = []
    list_display = ('title', 'price')
    search_fields = ('title', 'price')
    ordering = ('-price',)
    list_per_page = 10
    prepopulated_fields = {"slug" : ("title", )}

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductComment)