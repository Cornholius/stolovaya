from django import forms
from .models import Food
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User





class FoodForm(forms.ModelForm):

    class Meta:
        model = Food
        fields = ('name', 'description', 'price', 'type')

    def __init__(self, *args, **kwargs):
        super(FoodForm, self).__init__(*args, **kwargs)
        # self.fields['name'].label = "Заголовок заметки"
        # self.fields['type'].label = "Текст заметки"