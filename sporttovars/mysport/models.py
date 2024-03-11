
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Brend(models.Model):
    name = models.CharField(max_length=15)
    img_brend = models.ImageField(upload_to='D:\projects\kursov_futurediplom\sporttovars\static\imgmod')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def get_absolute_url_brend(self):
        return f'/tovars/{self.name}'

class Color(models.Model):
    color = models.CharField(max_length=20)


    def __str__(self):
        return self.color

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'


class Sport_item(models.Model):
    name = models.CharField(max_length=30)
    brend = models.ForeignKey(Brend,on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.TextField()
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='D:\projects\kursov_futurediplom\sporttovars\static\imgmod')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Characheristic(models.Model):
    season_year = models.CharField(max_length=15)
    country_crator = models.CharField(max_length=25)
    material = models.CharField(max_length=30)
    vid_sport = models.CharField(max_length=50)
    good = models.OneToOneField(Sport_item,on_delete=models.CASCADE)

    def __str__(self):
        return self.good.name

    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'


class Size(models.Model):
    size = models.CharField(max_length=10)
    good = models.ForeignKey(Sport_item,on_delete = models.CASCADE)

    def __str__(self):
        return self.good.name

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Subcat(MPTTModel):
    name = models.CharField(max_length=25)
    cat = models.ForeignKey(Category,on_delete=models.CASCADE)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    img_subcatcat = models.ImageField(null=True,upload_to='D:\projects\kursov_futurediplom\sporttovars\static\imgmod')
    subcutscats = models.ManyToManyField(Sport_item,blank=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сабкатегория'
        verbose_name_plural = 'Сабкатегории'

    def get_absolute_url(self):
        return f'/subcat/{self.id}'

    def get_absolute_url1(self):
        return f'/tovars/{self.id}'

    def get_absolute_url3(self):
        return f'/tovars/{self.id}/sort/'

class Feedback(models.Model):
    email = models.CharField(max_length=80)
    text = models.TextField()

class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    number_phone = models.CharField(max_length=25)
    address = models.CharField(max_length=200, null=True)
    postal_index = models.CharField(max_length=20)

class Order(models.Model):
    user = models.ForeignKey(User,null=True, blank=True,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items',on_delete=models.CASCADE)
    sport_item = models.ForeignKey(Sport_item, related_name='order_items',on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

# class Subcat(models.Model):
#     name = models.CharField(max_length=25)
#     cat = models.ForeignKey(Category,on_delete=models.CASCADE)
#     parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
#     img_subcatcat = models.ImageField(upload_to='D:\projects\kursov_futurediplom\sporttovars\static\imgmod', null=True)
#     subcutscats = models.ManyToManyField(Sport_item)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Сабкатегория'
#         verbose_name_plural = 'Сабкатегории'

# class Subcat_cat(models.Model):
#     name = models.CharField(max_length=25)
#     subcat = models.ForeignKey(Subcat,on_delete=models.CASCADE,null=True)
#     subcutscats = models.ManyToManyField(Sport_item)
#     img_subcatcat = models.ImageField(upload_to='D:\projects\kursov_futurediplom\sporttovars\static\imgmod')
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Категория сабкатегории'
#         verbose_name_plural = 'Категории сабкатегорий'