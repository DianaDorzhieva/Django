from django.contrib import admin
from materials.models import Materials


# Register your models here.
@admin.register(Materials)
class MaterialsAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published')
