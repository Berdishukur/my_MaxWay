# Generated by Django 4.2.3 on 2023-07-31 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
