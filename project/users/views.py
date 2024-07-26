from django.shortcuts import render, redirect , get_object_or_404
from django.contrib import messages
from .forms import UserForm, LoginForm
from .models import UserModel


def index(request):
    if 'username' in request.session:
        return redirect('hotel_list')
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User registered successfully!')
            return redirect('login')
    else:
        form = UserForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = UserModel.objects.filter(username=username, password=password).first()
            if user:
                request.session['username'] = username
                return redirect('hotel_list')
            else:
                messages.error(request, 'Invalid credentials!')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    if 'username' in request.session:
        del request.session['username']
    return redirect('login')

