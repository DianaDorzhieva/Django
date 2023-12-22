from materials.models import Materials
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        Materials.objects.all().delete()
        materials_for_create = []

        materials_list = [{"title": "Саморазвитие",
                           "body": "Как важно развивать ум",
                           "slug": "Вкусные,сладкие",
                           "img": "",
                           "date_creation": "",
                           "is_published": True,
                           "count_view": 0
                           },

                          {"title": "Отдых",
                           "body": "Как важно уметь отдыхать и расслабляться",
                           "slug": "Вкусные,сладкие",
                           "img": "",
                           "date_creation": "",
                           "is_published": True,
                           "count_view": 0
                           },

                          {"title": "Cон и еда",
                           "body": "Надо хорошо спать",
                           "slug": "",
                           "img": "",
                           "date_creation": "",
                           "is_published": False,
                           "count_view": 0
                           }
                          ]
        for item in materials_list:
            materials_for_create.append(Materials(**item))
        Materials.objects.bulk_create(materials_for_create)

        Materials.objects.bulk_create(materials_for_create)
