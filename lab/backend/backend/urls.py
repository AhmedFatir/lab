"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# backend/urls.py


from django.contrib import admin
from django.urls import path
from login.views import signup_view, login_view, welcome_view, custom_logout_view
from login.views import check_user_exists

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup_view, name='signup'),  # Directly map signup view
    path('login/', login_view, name='login'),  # Directly map login view
    path('welcome/', welcome_view, name='welcome'),  # Directly map welcome view
    path('logout/', custom_logout_view, name='logout'),
    path('check_user/<str:username>/', check_user_exists, name='check_user'),
]

