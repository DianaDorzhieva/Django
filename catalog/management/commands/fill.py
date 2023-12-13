from catalog.models import Product, Category
from django.core.management import BaseCommand
import json


class Command(BaseCommand):
    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()
        category_for_create = []
        product_for_create = []

        with open('data.json', encoding="UTF-8") as file:
            data_info = json.load(file)
            for item in data_info:
                if item["model"] == "catalog.category":
                    category_for_create.append(Category(**item['fields']))
                else:
                    product_for_create.append(Product(**item['fields']))

        Category.objects.bulk_create(category_for_create)
        Product.objects.bulk_create(product_for_create)
