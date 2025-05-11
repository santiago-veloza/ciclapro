from django.contrib import admin
from .models import Venta, Factura

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'fecha', 'total')
    search_fields = ('cliente__username',)
    list_filter = ('fecha',)

    def has_add_permission(self, request):
        return False  # 🔒 No permite añadir desde el admin


@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ('venta', 'fecha_emision', 'descripcion')
    search_fields = ('descripcion',)

    def has_add_permission(self, request):
        return False  # 🔒 No permite añadir desde el admin
