from django.db import models

# Create your models here.

class Brend(models.Model):
    name = models.CharField(max_length=15)
    img_brend = models.ImageField(upload_to='D:\projects\kursov_futurediplom\sporttovars\static\imgmod')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

class Sport_item(models.Model):
    name = models.CharField(max_length=30)
    brend = models.ForeignKey(Brend,on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.TextField()
    img = models.ImageField(upload_to='D:\projects\kursov_futurediplom\sporttovars\static\imgmod')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class Size(models.Model):
    size = models.IntegerField()
    good = models.ForeignKey(Sport_item,on_delete = models.CASCADE)

    def __str__(self):
        return self.good.name

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'

class Color(models.Model):
    color = models.CharField(max_length=20)
    good = models.ForeignKey(Sport_item,on_delete = models.CASCADE)

    def __str__(self):
        return self.color

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

class Characheristic(models.Model):
    season_year = models.CharField(max_length=5)
    country_crator = models.CharField(max_length=25)
    vid_sport = models.CharField(max_length=20)
    good = models.OneToOneField(Sport_item,on_delete=models.CASCADE)

    def __str__(self):
        return self.good.name

    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Subcat(models.Model):
    name = models.CharField(max_length=25)
    cat = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сабкатегория'
        verbose_name_plural = 'Сабкатегории'

class Subcat_cat(models.Model):
    name = models.CharField(max_length=25)
    subcat = models.ForeignKey(Subcat,on_delete=models.CASCADE,null=True)
    subcutscats = models.ManyToManyField(Sport_item)
    img_subcatcat = models.ImageField(upload_to='D:\projects\kursov_futurediplom\sporttovars\static\imgmod')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория сабкатегории'
        verbose_name_plural = 'Категории сабкатегорий'