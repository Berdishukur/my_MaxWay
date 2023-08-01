from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import *
from . import services
def login_required_decorator(func):
    return login_required(func,login_url='login_page')

@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect("login_page")

login_required_decorator
def login_page(request):
    if request.POST:
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, password=password, username=username)
        if user is not None:
            login(request, user)
            return redirect("home_page")

    return render(request, 'dashboard/login.html')
@login_required_decorator
def home_page(request):
    categories=services.get_categories()
    products=services.get_product()
    ctx={
        'counts' : {
            'categories':len(categories),
            'products':len(products),
        }
    }
    return render(request, 'dashboard/index.html', ctx)
@login_required_decorator
def category_list(request):
    categories=services.get_categories()
    print(categories)
    ctx={
        "categories":categories
    }
    return render(request,'dashboard/category/list.html',ctx)
@login_required_decorator
def category_create(request):
    model = Category()
    form = CategoryForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions',[])
        actions += [f"You created category: {request.POST.get('name')}"]
        request.session["actions"] = actions

        category_count = request.session.get('category_count', 0)
        category_count +=1
        request.session["category_count"] = category_count

        return redirect('category_list')
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, 'dashboard/category/form.html', ctx)


@login_required_decorator
def category_edit(request,pk):
    model = Category.objects.get(pk=pk)
    form = CategoryForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f"You edited category: {request.POST.get('name')}"]
        request.session["actions"] = actions
        return redirect('category_list')
    ctx = {
        "model":model,
        "form":form
    }
    return render(request,'dashboard/category/form.html',ctx)

@login_required_decorator
def category_delete(request,pk):
    model = Category.objects.get(pk=pk)
    model.delete()
    return redirect('category_list')
@login_required_decorator
def product_delete(request,pk):
    model = Product.objects.get(pk=pk)
    model.delete()
    return redirect('category_list')
@login_required_decorator
def product_edit(request,pk):
    model = Product.objects.get(pk=pk)
    form = ProductForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f"You edited product: {request.POST.get('name')}"]
        request.session["actions"] = actions
        return redirect('product_list')
    ctx = {
        "model":model,
        "form":form
    }
    return render(request,'dashboard/product/form.html',ctx)

@login_required_decorator
def product_list(request):
    products=services.get_product()
    ctx={
        'products':products
    }
    return render(request,'dashboard/product/list.html',ctx)
@login_required_decorator
def product_create(request):
    model=Product()
    form=ProductForm(request.POST or None,instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f"You created product: {request.POST.get('name')}"]
        request.session["actions"] = actions

        product_count = request.session.get('product_count', 0)
        product_count += 1
        request.session["product_count"] = product_count

        return redirect('product_list')
    ctx={
        "model":model,
        "form":form
    }
    return render(request,'dashboard/product/form.html',ctx)





@login_required_decorator
def profile(request):
    return render(request,'dashboard/profile.html')