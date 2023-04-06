from django.contrib import admin

from sample.models import Marca, Producto


class MarcaAdmin(admin.ModelAdmin):
    model = Marca
    list_display = ("id", "nombre")
    search_fields = ("nombre",)


class ProductoAdmin(admin.ModelAdmin):
    model = Producto
    list_display = ("id", "nombre", "precio", "marca")
    search_fields = ("nombre", "marca__nombre")
    list_filter = ("marca__nombre",)
    readonly_fields = ("precio",)


admin.site.register(Marca, MarcaAdmin)
admin.site.register(Producto, ProductoAdmin)
