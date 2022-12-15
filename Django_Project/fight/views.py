from django.shortcuts import render
from .tests import prenom, nom
# Create your views here.

def index(request):
    return render(request, "index.html", context={"prenom": prenom, "nom": nom})