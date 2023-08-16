from django.contrib import admin
from AppPagina import models

# Register your models here.

admin.site.register(models.Articulo)
admin.site.register(models.Cliente)
admin.site.register(models.Vendedor)

