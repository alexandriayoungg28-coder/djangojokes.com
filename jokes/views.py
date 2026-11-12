from django.urls import reverse_lazy

from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView
)

from .models import Joke

class JokeCreateView(CreateView):
    model = Joke
    fields = ['question', 'answer']


class JokeDeleteView(DeleteView):
    model = Joke
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('jokes:list')


class JokeDetailView(DetailView):
    model = Joke
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class JokeListView(ListView):
    model = Joke


class JokeUpdateView(UpdateView):
    model = Joke
    fields = ['question', 'answer']
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
