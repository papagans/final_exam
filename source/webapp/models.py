from django.db import models
from django.contrib.auth.models import User


class Files(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='announce_author', verbose_name='Автор',
                               null=True, blank=True, default=None)
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name='Подпись')
    file = models.FileField(null=True, blank=True, upload_to='uploads', verbose_name='Файл')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    counter = models.BigIntegerField(default=0, verbose_name='Счетчик')

    # def __str__(self):
    #     return self.author

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
        ordering = ['-created_at']
# Create your models here.
