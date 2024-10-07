from django.contrib import admin
from .models import TareaFacultad
from .models import User  

admin.site.register(User)

@admin.register(TareaFacultad)
class TareaFacultadAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_entrega', 'estado')
    list_filter = ('estado', 'fecha_entrega')
    search_fields = ('titulo', 'descripcion')
