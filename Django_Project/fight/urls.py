from django.contrib import admin
from django.urls import path
from .views import travel

urlpatterns = [
    path('', travel, name='fight-travel')
]