from django.db import models

NULLABLE = {'blank': True, 'null': True}
class Materials(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    body = models.TextField(verbose_name='содержимое')
    slug = models.CharField(max_length=150, verbose_name='слаг', **NULLABLE)
    img = models.ImageField(upload_to='materials/', verbose_name='изображение', **NULLABLE)
    date_creation = models.DateTimeField(verbose_name='дата создания', **NULLABLE)
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    count_view = models.IntegerField(default=0, verbose_name='просмотры')


    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'

    def __str__(self):
        return self.title
