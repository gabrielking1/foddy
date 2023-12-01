from django.shortcuts import render
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import ProductForm, CateForm
from .models import Category, Product
from Myapp.filters import FoodFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def index(request):
    cat = Category.objects.prefetch_related('product_set').all()
    product = Product.objects.all()
    pizza =  Product.objects.filter(choice__name__icontains="Pizza")
    burger = Product.objects.filter(choice__name__icontains="Burger")
    sandwiches= Product.objects.filter(choice__name__icontains="Sandwiches")
    pasta = Product.objects.filter(choice__name__icontains="Pasta")
    
    return render(request,'index.html',{'category':cat, 'product':product, 'pizza':pizza,
                'burger':burger,'sandwiches':sandwiches,'pasta':pasta})


def product(request):

    if request.user.is_superuser:
   

        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES)
            
            if form.is_valid():
                messages.success(request, 'product added successfully')
                form.save()
            
            
                return redirect('/product/')
            else:
                print("something went wrong")
        else:
            form = ProductForm()
        
        return render(request, 'product.html', {'form': form})
    else:
        messages.info(request, "You are not authorized ")
        return redirect('index')
    
def category(request):

    if request.user.is_superuser:
   

        if request.method == 'POST':
            form = CateForm(request.POST, request.FILES)
            
            if form.is_valid():
                messages.success(request, 'category added successfully')
                form.save()
            
            
                return redirect('/category/')
            else:
                print("something went wrong")
        else:
            form = CateForm()
        
        return render(request, 'cate.html', {'form': form})
    else:
        messages.info(request, "You are not authorized ")
        return redirect('index')
    
def food(request):
    product = Product.objects.all()
    myfilter = FoodFilter(request.GET, queryset=product)
        
        
    page = request.GET.get('page', 1)

    paginator = Paginator(myfilter.qs, 2)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return render(request, 'food.html', {'product':product,
                  'myfilter':myfilter,
                  'page_obj':page_obj})
