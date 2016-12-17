from django.utils import timezone
from .models import Product
from django.shortcuts import render, get_object_or_404 , redirect
from .forms import ProductForm

def list_products(request):
    List = Product.objects.all()
    context = {'List':List}
    return render(request, 'ecommerce/list_products.html',context)

def detail_product(request, pk):
    obj = Product.objects.get(id=pk)
    print(obj)
    return  render(request,'detail_product.html', {'obj':obj})

def add_product(request):
    form = ProductForm()
    context = {'form':form}
    return render(request, 'ecommerce/add_product.html', context)	

def save_product(request):
	if request.method == "POST":	
		form = ProductForm(request.POST, request.FILES)
		print(form.errors)
       		if form.is_valid():
			form.save()
       			context = {'form':form}
  			print form.errors
	       		return render(request, 'ecommerce/save.html', context)
	else:
    		form = ProductForm()
		print(form.errors)
  		return render(request, 'ecommerce/add_product.html', {'form': form})

