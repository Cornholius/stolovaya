from django.shortcuts import render
from django.views import View
from .models import Food, Category, Weeks, Days
from cart.forms import CartAddProductForm


color = ('994848', '48994b', '7f4899', '486e99', 'a63223', '9ba623', '23a66f', '948e8f', )
check = 'True'

class MainPage(View):

    def get(self, request):
        week = Weeks.objects.get(id=1)
        return render(request, 'main/mainpage.html', {'Monday': week.days.get(day='Понедельник').food.all(),
                                                      'Tuesday': week.days.get(day='Вторник').food.all(),
                                                      'Wednesday': week.days.get(day='Среда').food.all(),
                                                      'Thursday': week.days.get(day='Четверг').food.all(),
                                                      'Friday': week.days.get(day='Пятница').food.all()})


class Menu(View):

    def get(self, request, menu_type=None):
        if menu_type:
            category = Category.objects.get(slug=menu_type).id
            menu_list = Food.objects.filter(category_id=category)
            cart_form = CartAddProductForm
            return render(request, 'main/menulist.html', {'form': menu_list, 'cart_product_form': cart_form})


class TodayInMenu(View):

    def get(self, request):
        menu_list = Food.objects.filter(category_id='1')
        cart_form = CartAddProductForm
        return render(request, 'main/today.html', {'form': menu_list, 'cart_product_form': cart_form})
