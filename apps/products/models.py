from django.db import models
from apps.categories.models import Category
from apps.users.models import User

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    
    main_product_image = models.ImageField(upload_to = 'main_product_image', blank = True, null = True)
    description = models.TextField()
    specs = models.TextField(default="")
    price = models.FloatField()
    rating = models.IntegerField(default=0)
    count = models.IntegerField()
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_category')
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

class ProductComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_product")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_comment" )
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = "Коментарий"
        verbose_name_plural = "Коментарии"