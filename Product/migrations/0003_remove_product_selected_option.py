# Generated by Django 5.0 on 2023-12-25 03:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_remove_product_category_remove_product_category_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='selected_option',
        ),
    ]
