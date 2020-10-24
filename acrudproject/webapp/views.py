from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView
from django.shortcuts import render
from webapp.models import Blog
from django.views.generic.edit import CreateView,UpdateView,DeleteView
# Create your views here.
class Listview(object):
    pass

class BlogListview(ListView):
    model = Blog
    template_name = 'base.html'

class BlogDetailview(DetailView):
    model = Blog
    template_name = 'detail.html'
    context_object_name = 'batman'

class BlogCreateview(CreateView):
    model = Blog
    template_name = 'blog_create.html'
    fields = '__all__'

class BlogUpdateview(UpdateView):
    model = Blog
    template_name = 'blog_update.html'
    fields = ['title','text']

class BlogDeleteview(DeleteView):
    model = Blog
    template_name = 'blog_delete.html'
    context_object_name = 'batman'
    success_url = reverse_lazy('home')

