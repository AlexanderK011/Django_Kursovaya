from decimal import Decimal
from django.conf import settings
from mysport.models import Sport_item


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, sport_item, quantity=1, update_quantity=False):
        tovar_id = str(sport_item.id)
        if tovar_id not in self.cart:
            self.cart[tovar_id] = {'quantity': 0,
                                     'price': str(sport_item.price)}
        if update_quantity:
            self.cart[tovar_id]['quantity'] = quantity
        else:
            self.cart[tovar_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, sport_item):
        tovar_id = str(sport_item.id)
        if tovar_id in self.cart:
            del self.cart[tovar_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Sport_item.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product
        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True