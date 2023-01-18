from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse

# Create your views here.

def curso(self):
    
    curso = Curso(nombre = "Desarrollo Web", camada = "102392")
    curso.save()
    documentodetexto = f'Curso :{curso.nombre}, Camada: {curso.camada}'

    return HttpResponse(documentodetexto)
