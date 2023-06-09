from django.shortcuts import HttpResponse, redirect, render

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


def modificar_producto(request, producto_id):
    marcas = Marca.objects.all()
    producto = Producto.objects.get(id=producto_id)

    context = {
        "marcas": marcas,
        "producto": producto
    }

    if request.POST:
        nombre = request.POST['nombre']
        precio = request.POST['precio']
        marca_id = request.POST['marca']

        producto.nombre = nombre
        producto.precio = precio
        producto.marca_id = marca_id
        producto.save()

    return render(request, "sample/modificar_producto.html", context)


def eliminar_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    producto.delete()

    return redirect("listado_productos")


def desactivar_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    producto.activo = False
    producto.save()

    return redirect("listado_productos")


def activar_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    producto.activo = True
    producto.save()

    return redirect("listado_productos")