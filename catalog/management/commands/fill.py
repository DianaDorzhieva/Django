from catalog.models import Product, Category
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()
        category_for_create = []
        product_for_create = []


        category_list = [{"pk": 1,
                          "name": "ягоды",
                          "description": "Вкусные,сладкие"},

                         {"pk": 2,
                          "name": "грибы",
                          "description": "Норм"}
                         ]
        for item in category_list:
            category_for_create.append(Category(**item))
        Category.objects.bulk_create(category_for_create)

        product_info = [
            {"name": "мухомор",
             "description": "Есть нельзя, но он красивый",
             "image": "products/1.jpg",
             "category_id": 2,
             "price_one": 70,
             "date_creation": "2023-12-12T11:35:16Z",
             "date_last_modification": "2023-12-12T11:35:22Z"},

            {"name": "черешня",
             "description": "Ах какая вкусная",
             "image": "products/2.jpg",
             "category_id": 2,
             "price_one": 7000,
             "date_creation": "2023-12-12T11:35:16Z",
             "date_last_modification": "2023-12-12T11:35:22Z"},

            {"name": "земляника",
             "description": "Вкусная, сладкая, притягательно ароматная ягода",
             "image": "products/3.jpg",
             "category_id": 1,
             "price_one": 5000,
             "date_creation": "2023-12-12T11:35:16Z",
             "date_last_modification": "2023-12-12T11:35:22Z"},

            {"name": "клюква",
             "description": "Природный антибиотик",
             "image": "products/4.jpg",
             "category_id": 1,
             "price_one": 9000,
             "date_creation": "2023-12-12T11:35:16Z",
             "date_last_modification": "2023-12-12T11:35:22Z"}

        ]
        for item_product in product_info:
            product_for_create.append(Product(**item_product))

        Product.objects.bulk_create(product_for_create)



