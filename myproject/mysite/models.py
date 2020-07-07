from django.db import models

# Create your models here.
class Category(models.Model):
        name = models.CharField(verbose_name='Название',
                                max_length=255,
                                default=' ')

        def __str__(self):
            return self.name

        class Meta:
            verbose_name = 'Категория'
            verbose_name_plural = 'Категории'


class Product(models.Model):
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 null=True,
                                 blank=True,
                               verbose_name='Категория')

    name = models.CharField(verbose_name='Название',
                            max_length=255,
                            default=' ')

    desc = models.CharField(verbose_name='Описание',
                            max_length=255,
                            blank=True,
                            default=' ')

    is_active = models.BooleanField(verbose_name='Доступен',
                                    default=True)

    kount = models.FloatField(default=0,
                              verbose_name='Остаток')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
