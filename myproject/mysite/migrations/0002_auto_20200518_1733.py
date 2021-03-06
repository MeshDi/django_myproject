# Generated by Django 2.2 on 2020-05-18 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Доступен'),
        ),
        migrations.AddField(
            model_name='product',
            name='kount',
            field=models.FloatField(default=0, verbose_name='Остаток'),
        ),
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.CharField(blank=True, default=' ', max_length=255, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default=' ', max_length=255, verbose_name='Название'),
        ),
    ]
