from django.shortcuts import render
from blog.models import Configuracion
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from blog.models import Post
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
def index (request):
    configuracion = Configuracion.objects.first()
    return render(request, 'blog/index.html',{'configuracion':configuracion})

class ListPost(ListView):
    model=Post
class SearchPostByName(ListView):
    def get_queryset(self):
        post_title=self.request.GET.get('post-title')
        return Post.objects.filter(title_icontains=blog_title)
class BlogLogin(LoginView):
    template_name= 'blog/blog_login.html'
    next_page = reverse_lazy("list=-post")
class BlogLogout(LogoutView):
    template_name='blog/blog_logout.html'
# Create your views here.
