from django import forms
from .models import Food


class FoodForm(forms.ModelForm):

    class Meta:
        model = Food
        fields = ('name', 'description', 'price', 'type')

    def __init__(self, *args, **kwargs):
        super(FoodForm, self).__init__(*args, **kwargs)
