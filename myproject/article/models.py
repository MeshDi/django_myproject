from django.db import models



# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=255,verbose_name='Имя')
    email = models.EmailField(verbose_name='Почта')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

class Article(models.Model):
    title = models.CharField(max_length=120,verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    body = models.TextField(verbose_name='Тело')
    author = models.ForeignKey('Author', related_name='articles',
                               on_delete=models.CASCADE,verbose_name='Автор')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
