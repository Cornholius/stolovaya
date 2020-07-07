from django.shortcuts import render
from django.views import View
from .models import Food
from cart.forms import CartAddProductForm


color = ('994848', '48994b', '7f4899', '486e99', 'a63223', '9ba623', '23a66f', '948e8f', )
check = 'True'

class MainPage(View):

    def get(self, request):
        menu_list = Food.objects.all()
        cart_form = CartAddProductForm
        return render(request, 'main/menulist.html', {'form': menu_list, 'cart_product_form': cart_form})


class Menu(View):

    def get(self, request, menu_type=None):
        if menu_type:
            menu_list = Food.objects.filter(type=menu_type)
            cart_form = CartAddProductForm
            return render(request, 'main/menulist.html', {'form': menu_list, 'cart_product_form': cart_form})


class TodayInMenu(View):

    def get(self, request):
        menu_list = Food.objects.filter(type='salads')
        cart_form = CartAddProductForm
        return render(request, 'main/today.html', {'form': menu_list, 'cart_product_form': cart_form})
