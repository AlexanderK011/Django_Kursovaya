from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from mysport.models import Sport_item
from .cart import Cart
from .forms import CartAddProductForm
from mysport.views import menu


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
        'menu':menu
    }
    return render(request, 'mysport/cart.html', data)


# form = UserRegForm(request.POST)
#         profile_form = profileForm(request.POST)
#         if form.is_valid() and profile_form.is_valid():
#             user = form.save()
#             profile = profile_form.save(commit=False)
#             profile.user = user
#             profile.save()
#             messages.success(request,'Аккаунт создан')

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        user = request.user
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # очистка корзины
            cart.clear()
            return render(request, 'orders/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'orders/order/create.html',
                  {'cart': cart, 'form': form})