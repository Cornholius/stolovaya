from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    food_type = [('select', 'Выбери тип продукта'),
                 ('001', 'Первые блюда'),
                 ('002', 'Вторые блюда'),
                 ('003', 'Салаты')]
    type = models.CharField(max_length=20, choices=food_type, default='')
