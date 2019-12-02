from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.views.generic import TemplateView


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'


class BlogEditView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')


class BlogCinemaView(TemplateView):
    model = Post
    template_name = 'cinema.html'
    success_url = reverse_lazy('home')


class BlogMusicView(TemplateView):
    model = Post
    template_name = 'music.html'
    success_url = reverse_lazy('home')

class BlogMemView(TemplateView):
    model = Post
    template_name = 'mem.html'
    success_url = reverse_lazy('home')


class BlogMakersView(TemplateView):
    model = Post
    template_name = 'makers.html'
    success_url = reverse_lazy('home')


class BlogNewsView(TemplateView):
    model = Post
    template_name = 'news.html'
    success_url = reverse_lazy('home')


