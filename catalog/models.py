from django.contrib.auth import get_user_model
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

NULLABLE = {'blank': True, 'null': True}


# Create your models here.
class Product(models.Model):
    activity = [(True, 'Опубликовано'),
                (False, 'Неопубликовано')]

    name = models.CharField(max_length=250, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='категория',
                                 **NULLABLE)
    price_one = models.IntegerField(verbose_name='цена за штуку')
    date_creation = models.DateTimeField(verbose_name='дата создания')
    date_last_modification = models.DateTimeField(verbose_name='дата последнего изменения')
    is_published = models.BooleanField(verbose_name="Опубликовано", default=True, choices=activity)

    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, verbose_name='автор',
                               **NULLABLE)

    def __str__(self):
        return f" {self.name}:" \
               f" {self.description}"

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('price_one',)

        permissions = [
            ('can_change_is_published_permission', 'Can cancel product publication'),
            ('can_change_desc_permission', 'Can change product description'),
            ('can_change_category_permission', 'Can change product category'),
        ]


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')

    # created_at = models.DateTimeField(**NULLABLE) в терминале создала миграцию, применила. Потом откатила python manage.py migrate catalog 0001

    def __str__(self):
        return f"Категория продукта - {self.name}"

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)


class Version(models.Model):
    activity = [(True, 'Активно'),
                (False, 'Неактивно')]
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='продукт',
                                **NULLABLE)
    number = models.IntegerField(verbose_name='номер версии')
    name_version = models.CharField(max_length=250, verbose_name='название версии')
    active_version = models.BooleanField(verbose_name='признак текущей версии', choices=activity,
                                         default=False)

    def __str__(self):
        return f"{self.product} - версия номер {self.number}, название: {self.name_version} "

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'


@receiver(post_save, sender=Version)
def set_current_version(sender, instance, **kwargs):
    if instance.active_version:
        Version.objects.filter(product=instance.product).exclude(pk=instance.pk).update(
            active_version=False)
