from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone


class Post4(models.Model):

    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=None)
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст статьи')
    fulltext = models.TextField(verbose_name='Полный текст статьи')
    image = models.ImageField(verbose_name='Картинка')
    timage = models.ImageField(verbose_name='Картинка на сайте')
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
