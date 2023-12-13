from django.db import models

NULLABLE = {'blank': True, 'null': True}


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='категория', **NULLABLE)
    price_one = models.IntegerField(verbose_name='цена за штуку')
    date_creation = models.DateTimeField(verbose_name='дата создания')
    date_last_modification = models.DateTimeField(verbose_name='дата последнего изменения')

    def __str__(self):
        return f"Наименование - {self.name}: {self.description}"

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('price_one',)


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    #created_at = models.DateTimeField(**NULLABLE) в терминале создала миграцию, применила. Потом откатила python manage.py migrate catalog 0001

    def __str__(self):
        return f"Категория продукта - {self.name}"

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)
