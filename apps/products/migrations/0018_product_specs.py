# Generated by Django 4.0.4 on 2022-12-26 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_remove_product_memory_alter_product_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='specs',
            field=models.TextField(default=''),
        ),
    ]
