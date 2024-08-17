from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import logout
from .forms import CustomUserCreationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('welcome')  # Redirect to the welcome page
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, 'index.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Your account has been created successfully!")
                return redirect('welcome')
            else:
                messages.error(request, "There was an issue with logging you in after signup.")
        else:
            messages.error(request, "There was an error in the form. Please try again.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def welcome_view(request):
    user = request.user
    return render(request, 'welcome.html', {
        'full_name': user.get_full_name() or user.username,  # Fallback to username if full name isn't set
        'username': user.username,
        'email': user.email,
    })



def check_user_exists(request, username):
    user_exists = User.objects.filter(username=username).exists()

    if user_exists:
        return HttpResponse(f"User {username} exists!")
    else:
        return HttpResponse(f"User {username} does not exist!")

def custom_logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('login')  # Redirect to the login page

# Afatir8675@00*


# from django.contrib.auth.models import User
# user_exists = User.objects.filter(username='afatif').exists()
# if user_exists:
#     print("User exists!")
# else:
#     print("User does not exist.")
