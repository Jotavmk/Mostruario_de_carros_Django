from django.contrib import admin
from .models import Carro, Compra

@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ['marca', 'modelo', 'ano', 'preco', 'quilometragem', 'combustivel', 'disponivel', 'data_cadastro']
    list_filter = ['marca', 'combustivel', 'disponivel', 'ano']
    search_fields = ['marca', 'modelo', 'descricao']
    list_editable = ['preco', 'disponivel']
    date_hierarchy = 'data_cadastro'

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ['comprador', 'carro', 'preco_pago', 'data_compra']
    list_filter = ['data_compra']
    search_fields = ['comprador__username', 'carro__marca', 'carro__modelo']
    date_hierarchy = 'data_compra'
