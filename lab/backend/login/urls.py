# login/urls.py

from django.urls import path
from .views import signup_view, login_view, welcome_view

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('welcome/', welcome_view, name='welcome'),
]
