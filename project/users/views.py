from django.shortcuts import render, redirect , get_object_or_404
from django.contrib import messages
from .forms import UserForm, LoginForm,ProfileForm
from .models import UserModel,ProfileModel


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

def profile(request, user_id):
    user = get_object_or_404(UserModel, pk=user_id)
    try:
        profile = ProfileModel.objects.get(user=user)
    except ProfileModel.DoesNotExist:
        profile = None
    return render(request, 'profile.html', {'user': user, 'profile': profile})


def edit_profile(request, user_id):
    user = get_object_or_404(UserModel, pk=user_id)
    profile, created = ProfileModel.objects.get_or_create(user=user)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile', user_id=user_id)
    else:
        form = ProfileForm(instance=profile)
    
    return render(request, 'edit_profile.html', {'form': form, 'user': user})

def delete_profile(request, user_id):
    user = get_object_or_404(UserModel, pk=user_id)
    profile = get_object_or_404(ProfileModel, user=user)
    if request.method == 'POST':
        profile.delete()
        return redirect('hotel_list')  # Redirect to a page after deletion
    return render(request, 'confirm_delete.html', {'profile': profile})
