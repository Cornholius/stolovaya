from django import forms
from .models import Food, Feedback


class FoodForm(forms.ModelForm):

    class Meta:
        model = Food
        fields = ('name', 'description', 'price')

    def __init__(self, *args, **kwargs):
        super(FoodForm, self).__init__(*args, **kwargs)


class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = ('name', 'email', 'subject', 'message')

    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)