from django.contrib import admin
from django.urls import path

from accounts.views import LoginView, logout_view
from webapp.views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout')
]
