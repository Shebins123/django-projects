from django.shortcuts import render
from shop.models import category,product
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
def allprodCat(request):
    c = category.objects.all()
    return render(request,'category.html',{'c':c})
def allproducts(request,cslug):
    a = category.objects.get(slug=cslug)
    p=product.objects.filter(category__slug=cslug)
    return render(request,'view.html',{'p':p,'a':a})

def prodetail(request,bslug):
    b = product.objects.get(slug=bslug)
    return render(request,'detail.html',{'b':b})

def register(request):
    if(request.method=="POST"):
        a = request.POST['a']
        b = request.POST['b']
        c = request.POST['c']
        d = request.POST['d']
        e = request.POST['e']
        f = request.POST['f']
        if(e==f):
            user = User.objects.create_user(username=a,first_name=b,last_name=c,email=d,password=e)
            user.save()
            return allprodCat(request)
    return render(request,'register.html')

def user_login(request):
    if(request.method == "POST"):
        a = request.POST['a']
        e = request.POST['e']
        user = authenticate(username=a,password=e)
        if user:
            login(request,user)
            return allprodCat(request)
        else:
            messages.error(request,"invalid credentials")
    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return allprodCat(request)

