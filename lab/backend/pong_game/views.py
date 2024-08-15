from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import get_user_model

User = get_user_model()

def login_view(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username_or_email')
        password = request.POST.get('password')
        if '@' in username_or_email:
            try:
                user = User.objects.get(email=username_or_email)
                username = user.username
            except User.DoesNotExist:
                username = None
        else:
            username = username_or_email
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('welcome')
        else:
            messages.error(request, 'Invalid username/email or password.')
    return render(request, 'index.html')

User = get_user_model()

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Extract the form data
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')  # password1 and password2 are the same

            # Create the user using Django's create_user method
            user = User.objects.create_user(username=username, email=email, password=password)
            
            # Automatically log the user in after registration
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('welcome')
        else:
            # Log the form errors for debugging purposes
            print(form.errors)
            messages.error(request, 'Registration failed. Please check the form for errors.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'signup.html', {'form': form})

@login_required
def welcome_view(request):
    return render(request, 'welcome.html', {'user': request.user})
