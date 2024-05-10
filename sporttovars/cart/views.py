from django.forms import model_to_dict
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from mysport.models import Sport_item
from .cart import Cart
from .forms import CartAddProductForm, OrderCreateForm, AnonOrd
from mysport.views import menu

from mysport.models import OrderItem,AnonymCustomer



@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    tovar = get_object_or_404(Sport_item, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(sport_item=tovar,
                 # quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    tovar = get_object_or_404(Sport_item, id=product_id)
    cart.remove(tovar)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    data ={
        'cart':cart,
        'menu':menu,
        'title': 'Корзина'

    }
    return render(request, 'mysport/cart.html', data)

def order_create(request):
    cart = Cart(request)
    if not cart:
        return redirect('cart:cart_detail')
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        form1 = AnonOrd(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                order = form.save(commit=False)
                order.user = request.user
            else:
                anonuser = form1.save()
                order = form.save(commit=False)
                order.anonymuser = anonuser
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         sport_item=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            return redirect('cart:cart_detail')
    else:
        form = OrderCreateForm
        form_anonuser = AnonOrd
    return render(request, 'mysport/order_create.html',
                  {'cart': cart, 'form': form,'menu':menu,'form_anonuser':form_anonuser,'title':'Оформление заказа'})