from django.shortcuts import render
from ejemplo.models import Familiar

def index(request):
    return render(request, "ejemplo/saludar.html",{"nombre":"Leandro","apellido":"Ruiz"})


def monstrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "ejemplo/familiares.html", {"lista_familiares": lista_familiares})

def index_dos(request, nombre, apellido):
  return render(request, "ejemplo/saludar.html",{"nombre": nombre, "apellido":apellido,})

def index_tres(request):
  return render (request,"ejemplo/saludar.html",
  {"notas":[1,2,3,4,5,6,7,8]})
# Create your views here.
