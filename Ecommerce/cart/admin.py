from django.contrib import admin

from cart.models import cart,Account,Order
admin.site.register(cart)
admin.site.register(Account)
admin.site.register(Order)
