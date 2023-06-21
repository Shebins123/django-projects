from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from cart.models import cart,Account,Order
from shop.models import product
#from django.http import HttpResponse

@login_required
def cart_view(request):
    total=0
    try:
        user = request.user
        cartitems = cart.objects.filter(user=user)
        for i in cartitems:
            total += i.quantity*i.products.price
    except cart.DoesNotExist:
        pass
    return render(request,'cart.html',{'cart':cartitems,'total':total})

@login_required()
def add_cart(request,p):
    products = product.objects.get(id=p)
    user = request.user
    try:
        cart1 = cart.objects.get(products=products,user=user)
        if cart1.quantity < cart1.products.stock:
            cart1.quantity += 1
        cart1.save()
    except cart.DoesNotExist:
        cart1 = cart.objects.create(products=products,user=user,quantity=1)
        cart1.save()

    return redirect('cart:cart_view')

@login_required
def cart_remove(request,p):
    user = request.user
    products = product.objects.get(id=p)
    try:
        cart1 = cart.objects.get(user=user,products=products)
        if cart1.quantity > 1:
            cart1.quantity -= 1
            cart1.save()
        else:
            cart1.delete()
    except:
        pass
    return redirect('cart:cart_view')
@login_required
def full_remove(request,p):
    user = request.user
    products = product.objects.get(id=p)
    try:
        cart1 = cart.objects.get(user=user,products=products)
        cart1.delete()

    except:
        pass

    return redirect('cart:cart_view')

@login_required
def order(request):
    total = 0
    items = 0
    msg = 0
    if (request.method == "POST"):
        a = request.POST['a']
        b = request.POST['b']
        c = request.POST['c']
        user = request.user
        cart1 = cart.objects.filter(user=user)
        for i in cart1:
            total += i.quantity*i.products.price
            items+=i.quantity

        ac = Account.objects.get(acctnumber=c)
        if float(ac.amount) >= total:
                ac.amount = ac.amount-total
                ac.save()
                for i in cart1:
                    o = Order.objects.create(user=user,products=i.products,address=a,phone=b,order_status="paid",noofitems=i.quantity)
                    o.save()
                cart1.delete()
                msg ="ordered placed successfully"
                return render(request,'orderdetail.html',{'msg':msg,'total':total,'items':items})
        else:
                msg="insufficient amount.you cant place order."
                return render(request,'orderdetail.html',{'msg':msg})

    return render(request,'orderform.html')

def orderview(request):
    user = request.user
    o=Order.objects.filter(user=user,order_status="paid")
    return render(request,'orderview.html',{'o':o,'name':user.username})
