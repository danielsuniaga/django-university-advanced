from .models import Curso
from django.shortcuts import render
#from django.http import HttpResponse 


# Create your views here.

def home(request):

    cursosListados = Curso.objects.all()[:2]
    #return HttpResponse("<h1>Hola mundo</h1>")

    return render(request, "gestionCursos.html",{"cursos":cursosListados})