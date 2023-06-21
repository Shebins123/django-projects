from django.shortcuts import render
from shop.models import product
from django.db.models import Q
def search(request):
    products=None
    query=None
    if request.method=="POST":
        query=request.POST.get('q')
        if query:
            products=product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request,'search.html',{'query':query,'p':products})
