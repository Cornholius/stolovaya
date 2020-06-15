from django.shortcuts import render
from django.views import View
from .models import Food


class MainPage(View):

    def get(self, request):
        menu_list = Food.objects.all()
        return render(request, 'main/index.html', {'form': menu_list})


class Menu(View):

    def get(self, request, menu_type=None):
        if menu_type:
            menu_list = Food.objects.filter(type=menu_type)
            return render(request, 'main/index.html', {'form': menu_list})
