# Generated by Django 3.0.7 on 2020-06-25 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_product_subcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]