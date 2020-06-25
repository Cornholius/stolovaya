from django.shortcuts import render
from django.views import View
from .models import Food
from cart.forms import CartAddProductForm


class MainPage(View):

    def get(self, request):
        menu_list = Food.objects.all()
        cart_product_form = CartAddProductForm()

        return render(request, 'main/menulist.html', {'form': menu_list,
                                                      'cart_product_form': cart_product_form})


class Menu(View):

    def get(self, request, menu_type=None):
        if menu_type:
            menu_list = Food.objects.filter(type=menu_type)
            return render(request, 'main/menulist.html', {'form': menu_list})


class TodayInMenu(View):

    def get(self, request):
        menu_list = Food.objects.filter(type='salads')
        return render(request, 'main/today.html', {'form': menu_list})