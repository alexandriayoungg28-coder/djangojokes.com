from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView
)

from .forms import JokeForm
from .models import Joke

class JokeCreateView(LoginRequiredMixin, CreateView):
    model = Joke
    form_class = JokeForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class JokeDeleteView(UserPassesTestMixin, DeleteView):
    model = Joke
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('jokes:list')

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user


class JokeDetailView(DetailView):
    model = Joke
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class JokeListView(ListView):
    model = Joke


class JokeUpdateView(UserPassesTestMixin, UpdateView):
    model = Joke
    form_class = JokeForm
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user
