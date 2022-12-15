from django.contrib import admin
from django.urls import path
from .views import authentification

urlpatterns = [
    path('', authentification, name='authentification-connection')
]