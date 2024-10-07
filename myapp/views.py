from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import products

# Create your views here.

def index(request):
    return HttpResponse("This is my first blog")


def productsView(request):
    productsList = products.objects.all()
    context = {
        'products': productsList
    }
    return render(request, 'myapp/index.html', context)



def product_detail(request,id):
    product = products.objects.get(id=id)
    context = {
        'product': product
    }
    return render(request, 'myapp/detail.html', context)



def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        image = request.FILES['upload']
        product = products(name=name,price=price,desc=desc,image=image)
        product.save()
        return redirect('/products')
    return render(request, 'myapp/addproduct.html')


def update_product(request, id):
    product = products.objects.get(id=id)
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.desc = request.POST.get('desc')
        product.image = request.FILES['upload']
        product.save()
        return redirect('/products')
    context = {
        'product': product
    }
    return render(request, 'myapp/updateproduct.html',context)


def delete_product(request, id):
    product = products.objects.get(id=id)
    context = {
        'product': product
    }
    if request.method == 'POST':
        product.delete()
        return redirect('/products')
    return render(request, 'myapp/delete.html',context)