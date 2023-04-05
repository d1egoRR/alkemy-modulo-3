from django.shortcuts import HttpResponse


def saludar(request):
    return HttpResponse("Hola Mundo!! Esta es mi primer view")
