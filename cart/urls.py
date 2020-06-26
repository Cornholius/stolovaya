from django.urls import path
from .views import *


urlpatterns = [
    path('', CartView.as_view(), name='cart_detail'),
    path('add/<product_id>/', CartView.as_view(), name='cart_add'),
    path('remove/<product_id>/', CartView.as_view(), {'key': 'remove'}, name='cart_remove')
]