from django.contrib import admin
from django.urls import path

from accounts.views import LoginView, logout_view, RegisterView, ProfileView
from webapp.views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('register/', RegisterView.as_view(), name='register')
]
