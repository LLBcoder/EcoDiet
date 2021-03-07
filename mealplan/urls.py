from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('demo', views.demoPage, name='demo'),
    path('profile', views.profilePage, name='profile'),
    path('register', views.registerPage, name='register'),
    path('login', views.loginPage, name='login'),
    path('create', views.createMealplan, name='create'),
    path('logout', views.logoutPage, name='logout'),
]