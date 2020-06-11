from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    food_type = [('123', 'Выбери тип продукта'), ('123', '456'), ('2121', '3231')]
    type = models.CharField(max_length=20, choices=food_type, default='')
