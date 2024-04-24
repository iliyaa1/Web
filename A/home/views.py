from django.shortcuts import render,get_object_or_404
from django.views import View
from .models import Product,Category
from orders .forms import CartAddForm

class Home(View):
    def get(self,request,category_slug=None):
        products = Product.objects.filter()
        Categories = Category.objects.filter(is_sub=False)
        if category_slug:
            category = Category.objects.get(slug=category_slug)
            products = products.filter(category=category)
        return render(request,'home.html',{'products':products, 'Categories':Categories})
    

class ProductDetailView(View):
    def get(self,request,slug):
        product = get_object_or_404(Product,slug=slug)
        form = CartAddForm()
        return render(request, 'detail.html',{'product':product,'form':form})

