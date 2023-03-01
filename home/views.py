from django.http import HttpResponse


def index(request):
    return HttpResponse("Hola, me encuentro en la aplicación Home")

def home(request):
    return HttpResponse("Hola, esta es una nueva función de Home")