from django.db import models


class DatabaseConfig(models.Model):
    host = models.CharField(max_length=255)
    port = models.IntegerField()
    namedb = models.CharField(max_length=255)
    user = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    query = models.TextField()

    def __str__(self):
        return self.namedb

    class Meta:
        db_table = 'api_databaseconfig'  # Asegurar el nombre en la base de datos primaria


class ExtractionLog(models.Model):
    extraction_date = models.DateTimeField(auto_now_add=True)
    success = models.BooleanField()
    details = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Extraction on {self.extraction_date} - success {self.success}"

    class Meta:
        db_table = 'api_extractionlog'  # Asegurar el nombre en la base de datos primaria


# Modelos para secondary_db
class Factura(models.Model):
    fecha = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    cliente_id = models.IntegerField()
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'facturas'
        app_label = 'api'  # Especifica la app para enrutamiento


class ApiFactura(models.Model):
    fecha = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    cliente_id = models.IntegerField()
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'api_facturas'
        app_label = 'api'  # Especifica la app para enrutamiento
