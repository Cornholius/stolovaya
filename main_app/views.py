from django.shortcuts import render
from django.views import View
from .models import Food
from .forms import FoodForm

class MainPage(View):

    def get(self, request):
        form = FoodForm()
        return render(request, 'main/index.html', {'form': form})

