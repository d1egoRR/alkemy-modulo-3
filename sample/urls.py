from django.urls import path

from . import views

urlpatterns = [
    path('saludo/', views.saludar, name='saludar'),
    path('ejemplo/', views.ejemplo_template, name='ejemplo'),
]
