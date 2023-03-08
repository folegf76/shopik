from decimal import Decimal
from django.conf import settings
from shop.models import Product


class Wish:

    def __init__(self, request):
        self.session = request.session
        wish = self.session.get(settings.WISH_SESSION_ID)
        if not wish:
            wish = self.session[settings.WISH_SESSION_ID] = {}
        self.wish = wish

    def add(self, product):
        product_id = str(product.id)
        if product_id not in self.wish:
            self.wish[product_id] = {'quantity': 1}
        else:
            self.wish[product_id]['quantity'] = 1
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.wish:
            del self.wish[product_id]
            self.save()

    def clear(self):
        del self.session[settings.WISH_SESSION_ID]
        self.save()

    def __iter__(self):
        product_ids = self.wish.keys()
        products = Product.objects.filter(id__in=product_ids)
        wish = self.wish.copy()

        for product in products:
            wish[str(product.id)]['product'] = product

        for item in wish.values():
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.wish.values())