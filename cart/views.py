from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart
from .forms import CartAddProductForm
from main_app.models import Food
from django.views import View


class CartView(View):

    """
    В урлах висит дополнительный параметр 'key' с помощью него я могу вызвать класс cart_remove вместо get
    который вызывается по дефолту
    """
    def get(self, request, key=None, product_id=None):
        print('#1', product_id, request)
        if key == 'remove':
            self.cart_remove(request, product_id)
            return redirect('cart:cart_detail')

        else:
            print('#2', request.GET)
            cart = Cart(request)
            print('#3', request)
            return render(request, 'cart/detail.html', {'cart': cart})

    """
    при добавлении товара в корзину из основного меню в метод прилетает id блюда, записывается в корзину
    и возвращает обратно в ту же категорию, где и был человек. При нажатии кнопки "в корзину" в реквесте от кнопки 
    прилетает название кнопки которое = тип блюда т.е. его категория, и она же отправляется в редирект
    """
    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Food, id=product_id)
        form = CartAddProductForm(request.POST)
        print('#5', request.POST['type'])
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(product=product,
                     quantity=cd['quantity'],
                     update_quantity=cd['update'])
        return redirect('/menu/{}'.format(request.POST['type']))

    def cart_remove(self, request, product_id):
        print('#4', request.GET)
        cart = Cart(request)
        product = get_object_or_404(Food, id=product_id)
        cart.remove(product)
