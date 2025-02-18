from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('offers/', views.offers, name='offers'),
    path('news/', views.news, name='news'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),

    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),
    path('profile/', views.user_profile, name='profile'),
]
