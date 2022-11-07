from django.shortcuts import render
from blog.models import Configuracion
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from blog.models import Post
def index (request):
    configuracion = Configuracion.objects.first()
    return render(request, 'blog/index.html',{'configuracion':configuracion})

class ListPost(ListView):
    model=Post

class ListPost(ListView):
    model=Post
# Create your views here.
