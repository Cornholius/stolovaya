from django.shortcuts import render
from django.views import View
from .models import Food
from .forms import FoodForm

class MainPage(View):

    def get(self, request):
        menu = Food.objects.filter(type='002')
        print(menu)
        return render(request, 'main/index.html', {'form': menu})

