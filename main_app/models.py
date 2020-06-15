from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    food_type = [('select', 'Выбери тип продукта'),
                 ('First_course', 'Первые блюда'),
                 ('Second_course', 'Вторые блюда'),
                 ('Salads', 'Салаты')]
    type = models.CharField(max_length=20, choices=food_type, default='')
