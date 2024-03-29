# Generated by Django 4.2 on 2024-01-15 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_product_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_published',
            field=models.BooleanField(choices=[(True, 'Опубликовано'), (False, 'Неопубликовано')], default=True, verbose_name='Опубликовано'),
        ),
    ]
