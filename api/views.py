from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404

from sample.models import Producto


def listado_productos(request):
    """ retorna el listado de todos los productos en formato JSON """
    productos = list(Producto.objects.values())
    return JsonResponse(productos, safe=False)


def detalle_producto(request, producto_id):
    """ retorna un producto de acuerdo al ID """
    producto = get_object_or_404(Producto, id=producto_id)
    producto_dict = model_to_dict(producto)
    return JsonResponse(producto_dict, safe=False)
