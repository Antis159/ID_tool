from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register-page'),
    path('login/', auth_views.LoginView.as_view(template_name='login_register.html'), name='login-page'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout-page'),
    path('update/', views.update_user, name='user-page')

]
