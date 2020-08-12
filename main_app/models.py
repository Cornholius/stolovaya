from django.db import models


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

    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True)
    weight = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    unit = models.CharField(max_length=20, choices=unit_type, default='')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

    def __str__(self):
        return self.name


class Days(models.Model):
    day = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, unique=True)
    food = models.ManyToManyField(Food, verbose_name='тест1', related_name='test2', blank=True)

    def __str__(self):
        return self.day


class Weeks(models.Model):
    week_number = models.IntegerField(default=0)
    days = models.ManyToManyField(Days, verbose_name='тест3', related_name='test4', blank=True)
    food = models.ManyToManyField(Food, verbose_name='тест5', related_name='test6', blank=True)

    def __str__(self):
        return str(self.week_number)


class Feedback(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)

    class Meta:
        ordering = ('subject',)
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return 'Order {}'.format(self.id)
