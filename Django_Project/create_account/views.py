from django.shortcuts import render

# Create your views here.

def create(request):
    return render(request, "create_account/templates/create.html")