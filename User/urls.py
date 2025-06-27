from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_views, name='login'),
    path('signup/', views.signup_view, name='signup'),
]