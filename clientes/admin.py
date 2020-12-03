from django.contrib import admin
from clientes.models import Cliente

class Clientes(admin.ModelAdmin):
    list_display = ('id','nome','email')
    list_display_links = ('id','nome')
    search_fields = ('nome','email')

# Registro do crud de Cliente
admin.site.register(Cliente, Clientes)