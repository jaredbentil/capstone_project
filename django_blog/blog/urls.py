from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Using our custom registration view
    path('register/', views.register, name='register'),

    # Using Django's built-in Login and Logout views
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),

    # Using our custom profile view
    path('profile/', views.profile, name='profile'),
]
