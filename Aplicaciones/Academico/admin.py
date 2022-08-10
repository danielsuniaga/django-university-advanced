from django.contrib import admin
from .models import Curso, Docente

# Register your models here.

# admin.site.register(Curso)

@admin.register(Curso)

class CursoAdmin(admin.ModelAdmin):

    list_display = ('id','coloreado','creditos')

    #search_fields= ('nombre','creditos')

    #list_editable = ('nombre','creditos')

    #list_display_links = ('nombre')

    #list_filter = ('creditos',)

    #list_per_page = 1

    #exclude = ('creditos',)

    fieldsets = (

        (None, {
            'fields':('nombre','docente',)
        }),
        ('Advanced options',{
            'classes':('collapse','wide','extrapretty'),
            'fields':('creditos',)
        })
    )

    def datos(self, obj):

        return obj.nombre.upper()

    datos.short_description="CURSO (MAYUS)"

admin.site.register(Docente)