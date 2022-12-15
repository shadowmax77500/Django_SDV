from django.shortcuts import render

# Create your views here.

def authentification(request):
    return render(request, "authentification/templates/authentification.html")