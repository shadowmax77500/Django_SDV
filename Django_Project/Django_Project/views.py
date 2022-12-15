from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Bonjour tout le monde</h1>")