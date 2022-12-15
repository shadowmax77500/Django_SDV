from django.contrib import admin
from django.urls import path
from .views import create

urlpatterns = [
    path('', create, name='create_account-create')
]