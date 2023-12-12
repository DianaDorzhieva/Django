from catalog.models import Product
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        product_list = [
            {"name": "мухомор",
             "description": "есть нельзя, но он красивый",
             "image": "",
             "category": None, # не получается прописывать категорию, пайчарм выдает ошибку. Пробовала и цифрами и словами писать
             "price_one": 70,
             "date_creation": "2023-12-12T11:35:16Z",
             "date_last_modification": "2023-12-12T11:35:22Z"
             },

            {"name": "белый гриб",
             "description": "королевский гриб",
             "image": "",
             "category": None,
             "price_one": 7000,
             "date_creation": "2023-12-12T11:35:16Z",
             "date_last_modification": "2023-12-12T11:35:22Z"

             }
        ]
        product_for_create = []
        for product_item in product_list:
            product_for_create.append(Product(**product_item))

        Product.objects.bulk_create(product_for_create)
