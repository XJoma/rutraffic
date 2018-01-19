from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Company(models.Model):

    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст статьи')
    image = models.ImageField(verbose_name='Картинка')

    def __str__(self):
        return self.title
