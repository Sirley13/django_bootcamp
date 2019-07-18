from django.shortcuts import render
from django.http import HttpResponse
from pendientes.models import Tarea
from random import randint
# Create your views here.

def index(request):
    listita= Tarea.objects.all()
    persona = {
    "nombre": "Sirley",
     "edad": 28, 
     "hobbies":["aprender cosas nuevas","leer","crear paginas web"],
     "lista_tareas": listita,
    }
    return render(request,"inicio.html", persona) #retornamos el saludo

def tarea(request):
    return HttpResponse("hola soy la tarea")

def music(request):
    return HttpResponse("queeee vesss que ves cuando me veees")