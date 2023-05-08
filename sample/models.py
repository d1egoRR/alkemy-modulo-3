from django.db import models


class Marca(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField(default=0)
    marca = models.ForeignKey(
        Marca,
        related_name="productos",
        on_delete=models.CASCADE,
    )
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} ({self.marca})"
