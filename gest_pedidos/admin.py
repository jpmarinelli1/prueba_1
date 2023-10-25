from django.contrib import admin

from gest_pedidos.models import Clientes, Pedidos, Articulos

import datetime

class ClientesAdm(admin.ModelAdmin):
    def log(self,):
        return " %s " %(datetime.datetime.now())
    list_display = ("nombre","direccion",log)
    search_fields = (["nombre"]) # ("nombre",)
    list_filter = ("direccion",)

class PedidosAdm(admin.ModelAdmin):
    list_display = ("numero","fecha")
    list_filter = ("fecha",)
    date_hierarchy ="fecha"

class ArticulosAdm(admin.ModelAdmin):
    list_display = ("nombre","seccion","precio")
    search_fields = ("nombre",)

admin.site.register(Clientes,ClientesAdm)
admin.site.register(Pedidos,PedidosAdm)
admin.site.register(Articulos,ArticulosAdm)


# Register your models here.
