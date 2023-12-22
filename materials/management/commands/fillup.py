from materials.models import Materials
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        Materials.objects.all().delete()
        materials_for_create = []

        materials_list = [
            {
                "title": "Собаки",
                "body": "Милейшие пусечки",
                "slug": "",
                "img": "materials/1.jpg",
                "date_creation": "2023-12-12T11:35:16Z",
                "is_published": True,
                "count_view": 0
            },

            {
                "title": "Кошки",
                "body": "Пушистые милахи",
                "slug": "",
                "img": "materials/2.jpg",
                "date_creation": "2023-12-12T11:35:19Z",
                "is_published": True,
                "count_view": 0
            },

            {
                "title": "Совы",
                "body": "Приносят письма из Хогвартса",
                "slug": "",
                "img": "materials/3.jpg",
                "date_creation": "2023-12-12T11:35:18Z",
                "is_published": False,
                "count_view": 0
            }
        ]
        for item in materials_list:
            materials_for_create.append(Materials(**item))
        Materials.objects.bulk_create(materials_for_create)


