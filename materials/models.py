from django.db import models

class Materials(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    body = models.TextField(verbose_name='содержимое')

    class Meta:
        verbose_name = 'материал'
        verbose_name_plural = 'материалы'

    def __str__(self):
        return self.title
