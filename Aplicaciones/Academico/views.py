from .models import Curso
from django.views.generic import ListView
from django.shortcuts import render,redirect
#from django.http import HttpResponse 


# Create your views here.

def home(request):

    cursosListados = Curso.objects.all()[:2]
    #return HttpResponse("<h1>Hola mundo</h1>")

    data = {
        'titulo':'Gestión de Cursos',
        'cursos':cursosListados
    }
    #return render(request, "gestionCursos.html",{"cursos":cursosListados})

    return render(request,"gestionCursos.html",data)

class CursoListView(ListView):

    model = Curso

    template_name = 'gestionCursos.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['titulo'] = 'Gestion de Cursos'

        print(context)

        return context

def eliminar_curso(request,id):

    curso=Curso.objects.get(id=id)

    curso.delete()

    return redirect('/')

def registrar_curso(request):

    nombre = request.POST['txtNombre']

    creditos = request.POST['numCreditos']

    curso = Curso.Objects.create(nombre=nombre, creditos=creditos)

    return redirect('/')
