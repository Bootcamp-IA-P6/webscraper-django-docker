from django.contrib import admin
from .models import ScrapedData

@admin.register(ScrapedData)
class ScrapedDataAdmin(admin.ModelAdmin):
    # Esto configura las columnas que verás en la tabla
    list_display = ('title', 'url', 'created_at')
    # Añade un buscador por título
    search_fields = ('title',)
    # Añade un filtro lateral por fecha
    list_filter = ('created_at',)