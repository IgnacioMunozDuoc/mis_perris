from django.contrib import admin
from .models import Raza,Estado,Mascota,Genero,tipoVivienda,GeneroP,Region,Persona,tipoVivienda,Ciudad,Region,GeneroP
# Register your models here.

class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre','raza','genero','fechaIngreso','fechaNacimiento','imagen','estado')
    search_fields = ['raza']
    list_filter = ('raza',)

class PersonaAdmin(admin.ModelAdmin):
    list_display = ('correo','run','nombreP','telefono','fechaN','direccion','genero','region','ciudad','tipoV')
    search_fields = ['nombreP']
    list_filter = ('nombreP',)



admin.site.register(Raza)
admin.site.register(Estado)
admin.site.register(Mascota,MascotaAdmin)
admin.site.register(Genero)
admin.site.register(tipoVivienda)
admin.site.register(GeneroP)
admin.site.register(Region)
admin.site.register(Ciudad)
admin.site.register(Persona)
