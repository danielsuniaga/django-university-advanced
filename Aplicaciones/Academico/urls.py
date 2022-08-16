from django.urls import path
from Aplicaciones.Academico.views import CursoListView, eliminar_curso,registrar_curso,edicion_curso, editar_curso, contacto

urlpatterns = [
    
    path('',CursoListView.as_view(), name='gestion_cursos'),
    path('eliminarCurso/<int:id>',eliminar_curso),
    path('registrarCurso/', registrar_curso),
    path('edicionCurso/<int:id>',edicion_curso),
    path('editarCurso/',editar_curso),
    path('contacto/',contacto)
]