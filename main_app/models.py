from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.IntegerField()
    food_type = [('select', 'Выбери тип продукта'),
                 ('business_lunch', 'Бизнес ланч'),
                 ('soups', 'Супы'),
                 ('hot_course', 'Горячее'),
                 ('garnishes', 'Гарниры'),
                 ('salads', 'Салаты'),
                 ('drinks', 'Напитки')]
    type = models.CharField(max_length=20, choices=food_type, default='')
