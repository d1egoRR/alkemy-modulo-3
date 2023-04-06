from django.shortcuts import HttpResponse, render

from sample.models import Marca, Producto


def saludar(request):
    return HttpResponse("Hola Mundo!! Esta es mi primer view")


def ejemplo_template(request):
    context = {
        "nombre": "María",
        "apellido": "Torres",
        "edad": "35",
    }

    return render(request, "sample/ejemplo.html", context)


def listado_productos(request):
    productos = Producto.objects.all()

    return render(
        request,
        "sample/listado_productos.html",
        {"productos": productos}
    )


def nuevo_producto(request):
    marcas = Marca.objects.all()

    context = {
        "marcas": marcas
    }

    if request.POST:
        nombre = request.POST['nombre']
        precio = request.POST['precio']
        marca_id = request.POST['marca']

        Producto.objects.create(
            nombre=nombre,
            precio=precio,
            marca_id=marca_id
        )

    return render(request, "sample/nuevo_producto.html", context)
