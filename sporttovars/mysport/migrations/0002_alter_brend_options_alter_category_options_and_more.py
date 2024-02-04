# Generated by Django 5.0.1 on 2024-02-03 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysport', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brend',
            options={'verbose_name': 'Бренд', 'verbose_name_plural': 'Бренды'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='characheristic',
            options={'verbose_name': 'Характеристика', 'verbose_name_plural': 'Характеристики'},
        ),
        migrations.AlterModelOptions(
            name='color',
            options={'verbose_name': 'Цвет', 'verbose_name_plural': 'Цвета'},
        ),
        migrations.AlterModelOptions(
            name='size',
            options={'verbose_name': 'Размер', 'verbose_name_plural': 'Размеры'},
        ),
        migrations.AlterModelOptions(
            name='sport_item',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterModelOptions(
            name='subcat',
            options={'verbose_name': 'Сабкатегория', 'verbose_name_plural': 'Сабкатегории'},
        ),
        migrations.AlterModelOptions(
            name='subcat_cat',
            options={'verbose_name': 'Категория сабкатегории', 'verbose_name_plural': 'Категории сабкатегорий'},
        ),
        migrations.AlterField(
            model_name='brend',
            name='img_brend',
            field=models.ImageField(upload_to='D:\\projects\\kursov_futurediplom\\sporttovars\\static\\imgmod'),
        ),
        migrations.AlterField(
            model_name='sport_item',
            name='img',
            field=models.ImageField(upload_to='D:\\projects\\kursov_futurediplom\\sporttovars\\static\\imgmod'),
        ),
        migrations.AlterField(
            model_name='subcat_cat',
            name='img_subcatcat',
            field=models.ImageField(upload_to='D:\\projects\\kursov_futurediplom\\sporttovars\\static\\imgmod'),
        ),
    ]