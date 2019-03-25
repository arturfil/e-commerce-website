from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Product

def index(request): 
  text_var = 'This is my django web application'
  return HttpResponse(text_var)

# Category View
def allProductCategory(request, c_slug=None):
  c_page = None
  products = None
  
  if c_slug != None:
    c_page = get_object_or_404(Category,slug=c_slug)
    products = Product.objects.filter(category=c_page, available=True)
  else:
    products = Product.objects.all().filter(available=True)
  return render(request, 'shop/category.html',{'category':c_page,'products':products})

def ProdCatDetail(request, c_slug, product_slug):
  try:
    product = Product.objects.get(category__slug = c_slug, slug=product_slug)
  except Exception as e:
    raise e
  return render(request, 'shop/product.html',{'product':product})

def ProductCategoryDetail(request, c_slug, product_slug):
  try:
    product = Product.objects.get(category_slug=c_slug,slug=product_slug)
  except Exception as e:
    raise e
  return render(request, 'shop/product.html',{'product': product})