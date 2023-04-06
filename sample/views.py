from django.shortcuts import HttpResponse, render


def saludar(request):
    return HttpResponse("Hola Mundo!! Esta es mi primer view")


def ejemplo_template(request):
    context = {
        "nombre": "María",
        "apellido": "Torres",
        "edad": "35",
    }

    return render(request, "sample/ejemplo.html", context)
