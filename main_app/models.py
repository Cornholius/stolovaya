from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Food(models.Model):

    unit_type = [('', 'выбрать...'),
                 ('мл.', 'мл.'),
                 ('гр.', 'гр.'),
                 ('шт.', 'шт.')]

    category = models.ForeignKey(Category, verbose_name='Категории', related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='Название блюда')
    description = models.CharField(max_length=200, blank=True, verbose_name='Описание(не обязательно)')
    weight = models.IntegerField(default=0, verbose_name='Вес/Объём/Кол-во')
    price = models.IntegerField(default=0, verbose_name='Цена')
    unit = models.CharField(max_length=20, choices=unit_type, default='', verbose_name='Ед. измерения')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

    def __str__(self):
        return self.name


class Days(models.Model):
    text_menu = """
    Здесь выбираем СОСТАВ МЕНЮ на выбранный день недели, который будет отображаться при нажатие на кнопку с этим
    названием. Для того, чтобы выбрать несколько позиций зажимаем Ctrl и кликаем на нужные позиции."""
    text_lunch = """
    Здесь выбираем СОСТАВ ЛАНЧА на выбранный день недели, который будет отображаться при нажатие на кнопку с этим
    названием. Для того, чтобы выбрать несколько позиций зажимаем Ctrl и кликаем на нужные позиции."""
    day = models.CharField(max_length=20, editable=False)
    slug = models.SlugField(max_length=20, unique=True, editable=False)
    food = models.ManyToManyField(Food, verbose_name= 'Состав меню', related_name='test2', blank=True)
    lunch = models.ManyToManyField(Food, verbose_name= 'Состав Ланча', related_name='test21', blank=True)

    class Meta:
        # ordering = ('day',)
        verbose_name = 'Кнопка меню'
        verbose_name_plural = 'Кнопки меню'

    def __str__(self):
        return self.day


class Weeks(models.Model):
    week_number = models.IntegerField(default=0)
    days = models.ManyToManyField(Days, verbose_name='тест3', related_name='test4', blank=True)
    food = models.ManyToManyField(Food, verbose_name='тест5', related_name='test6', blank=True)

    def __str__(self):
        return str(self.week_number)


class Feedback(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    email = models.EmailField(max_length=254, verbose_name='Email')
    subject = models.CharField(max_length=100, verbose_name='Тема письма', default='')
    message = models.CharField(max_length=1000, verbose_name='Текст письма')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата написания')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
