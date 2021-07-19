from django.shortcuts import render
from .models import Product
# Create your views here.



def main(request):
    products = Product.objects.all()
    context ={'products':products}
    return render(request,'store.html',context)


def content(request,header):
    data=Product.objects.get(name=header)
    context = {'data':data,'header':header}
    if (data):
        return render(request,'content.html',context)
    else:
        return render(request,'store.html')

        

def checkout(request,header):
    data=Product.objects.get(name=header)
    context = {'data':data,'header':header}
    if (data):
        return render(request,'checkout.html',context)
    else:
        return render(request,'store.html')
    