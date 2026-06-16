from django.db import models


class Museo(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    ciudad = models.CharField(max_length=150)
    año_fundacion = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre


class GuiaMuseo(models.Model):
    museo = models.ForeignKey(
        Museo,
        on_delete=models.CASCADE,
        related_name="guias",
    )
    nombre_completo = models.CharField(max_length=250)
    años_experiencia_guia = models.PositiveIntegerField()
    idiomas_hablados = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre_completo


class Exhibicion(models.Model):
    guia = models.ForeignKey(
        GuiaMuseo,
        on_delete=models.PROTECT,
        related_name="exhibiciones",
    )
    titulo_exhibicion = models.CharField(max_length=250)
    duracion_meses = models.PositiveIntegerField()
    costo_produccion = models.DecimalField(max_digits=12, decimal_places=2)
    tematica = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo_exhibicion
