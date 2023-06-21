from cart.models import cart
def counter(request):
    item_count=0
    if request.user.is_authenticated:
        user=request.user
        try:
            cart1=cart.objects.filter(user=user)
            for i in cart1:
                item_count += i.quantity
        except cart.DoesNotExist:
            item_count=0
    return {'item_count':item_count}
