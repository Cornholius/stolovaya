from django.urls import path
from .views import *


urlpatterns = [
    path('', cart_detail, name='cart_detail'),
    path('add/<product_id>/', cart_add, name='cart_add'),
    path('remove/<product_id>/', cart_remove, name='cart_remove')
]