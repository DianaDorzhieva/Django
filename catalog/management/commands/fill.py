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
        Category.objects.bulk_create(category_for_create)

        product_info = [
            {"name": "мухомор",
             "description": "есть нельзя, но он красивый",
             "image": "",
             "category": Category(pk=2).save(),
             "price_one": 70,
             "date_creation": "2023-12-12T11:35:16Z",
             "date_last_modification": "2023-12-12T11:35:22Z"},

            {"name": "черешня",
             "description": "ах какая вкусная",
             "image": "",
             "category": Category(pk=1).save(),
             "price_one": 7000,
             "date_creation": "2023-12-12T11:35:16Z",
             "date_last_modification": "2023-12-12T11:35:22Z"}
        ]
        for item_product in product_info:
            product_for_create.append(Product(**item_product))

        Product.objects.bulk_create(product_for_create)
