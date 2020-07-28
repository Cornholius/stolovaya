from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from .models import Food, Category, Weeks, Days
from cart.forms import CartAddProductForm

color = ('994848', '48994b', '7f4899', '486e99', 'a63223', '9ba623', '23a66f', '948e8f',)
check = 'True'


class MainPage(TemplateView):
    template_name = 'main/mainpage.html'

    # def get(self, request):
    #     week = Weeks.objects.get(id=1)
    #     return render(request, 'main/mainpage.html')

    def get_context_data(self, **kwargs):
        context = super(MainPage, self).get_context_data(**kwargs)
        week = Weeks.objects.get(id=1)
        context['Monday'] = week.days.get(day='Понедельник').food.all()
        context['Tuesday'] = week.days.get(day='Вторник').food.all()
        context['Wednesday'] = week.days.get(day='Среда').food.all()
        context['Thursday'] = week.days.get(day='Четверг').food.all()
        context['Friday'] = week.days.get(day='Пятница').food.all()
        return context


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
