from django.shortcuts import render
from django.views import View
from .models import Food
from cart.forms import CartAddProductForm


class MainPage(View):

    def get(self, request):
        visible = 'display: none'
        return render(request, 'main/mainpage.html', {'visible': visible})


class Menu(View):

    def get(self, request, menu_type=None):
        if menu_type:
            menu_list = Food.objects.filter(type=menu_type)
            return render(request, 'main/menulist.html', {'form': menu_list})


class TodayInMenu(View):

    def get(self, request):
        menu_list = Food.objects.filter(type='salads')
        return render(request, 'main/today.html', {'form': menu_list})