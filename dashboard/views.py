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


def login_page(request):
    if request.POST:
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, password=password, username=username)
        if user is not None:
            login(request, user)
            return redirect("home_page")

    return render(request, 'login.html')
@login_required_decorator
def home_page(request):
    categories=services.get_categories()
    # kafedras = services.get_kafedra()
    # subjects = services.get_subject()
    # teachers = services.get_teacher()
    # groups = services.get_groups()
    # students = services.get_student()
    ctx={
        'counts' : {
            'categories':len(categories),
            # 'kafedras':len(kafedras),
            # 'subjects':len(subjects),
            # 'teachers':len(teachers),
            # 'groups':len(groups),
            # 'students':len(students)
        }
    }
    return render(request, 'index.html', ctx)
@login_required_decorator
def category_list(request):
    categories=services.get_categories()
    print(categories)
    ctx={
        "categories":categories
    }
    return render(request,'category/list.html',ctx)
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
    return render(request, 'category/form.html', ctx)


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
    return render(request,'category/form.html',ctx)

@login_required_decorator
def category_delete(request,pk):
    model = Category.objects.get(pk=pk)
    model.delete()
    return redirect('category_list')







@login_required_decorator
def profile(request):
    return render(request,'profile.html')