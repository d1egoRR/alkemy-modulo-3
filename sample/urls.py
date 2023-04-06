from django.urls import path

from . import views

urlpatterns = [
    path('saludo/', views.saludar, name='saludar'),
    path('ejemplo/', views.ejemplo_template, name='ejemplo'),
    path(
        'productos/listado',
        views.listado_productos,
        name='listado_productos'
    ),

    path(
        'productos/nuevo',
        views.nuevo_producto,
        name='nuevo_producto'
    ),
]
