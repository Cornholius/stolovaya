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
    # days = [('', 'выбери день'),
    #         ('Monday', 'понедельник'),
    #         ('Tuesday', 'вторник'),
    #         ('Wednesday', 'среда'),
    #         ('Thursday', 'четверг'),
    #         ('Friday', 'пятница')]
    #
    # week = [('', 'выбери неделю'),
    #         ('1', '1'),
    #         ('2', '2')]

    category = models.ForeignKey(Category, related_name='products',on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    weight = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    # week = models.CharField(max_length=20, choices=week, default='0')
    # day = models.CharField(max_length=20, choices=days, default='0')


    class Meta:
        ordering = ('name',)
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

    def __str__(self):
        return self.name
    # food_type = [('select', 'Выбери тип продукта'),
    #              ('business_lunch', 'Бизнес ланч'),
    #              ('soups', 'Супы'),
    #              ('hot_course', 'Горячее'),
    #              ('garnishes', 'Гарниры'),
    #              ('salads', 'Салаты'),
    #              ('drinks', 'Напитки')]
    # type = models.CharField(max_length=20, choices=food_type, default='')
