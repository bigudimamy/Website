from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import RegistrationForm, LoginForm, ProductsForm
from django.contrib.auth import authenticate, login, logout
from PIL import Image
from django.shortcuts import get_object_or_404

HttpResponse("<h1>Торговое предприятие</h1>")
def index(request):
    return render(request, 'enterprise/index.html')

def about(request):
    return render(request, 'enterprise/about.html')

def pat(request):
    return render(request, 'enterprise/pat.html')

def goods(request):
    categories = CategoryProducts.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'enterprise/goods.html', context)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            form.save()
            return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'enterprise/login.html', {'form': form})

def common_view(request):
    return render(request, 'common.html', {'user': request.user})

def create(request):
    error = ''
    if request.method == 'POST':
        form = ProductsForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.category = CategoryProducts.objects.get(id=request.POST['category'])
            image_file = request.FILES['image']
            product.image.save(image_file.name, image_file, save=True)
            product.save()
            return redirect('goods')
        else:
            error = 'Форма неверна'
    else:
        form = ProductsForm()

    data = {'form': form, 'error': error}
    return render(request, 'enterprise/create.html', data)

def delete(request, pk):
    product = get_object_or_404(Products, pk=pk)
    product.delete()
    return redirect('goods')



