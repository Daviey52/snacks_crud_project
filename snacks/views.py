from django.shortcuts import render
from .models import Snacks
from django.urls import reverse_lazy

from django.views.generic import ListView ,DetailView ,UpdateView, DeleteView, CreateView

class SnacksListView(ListView):
  template_name='snacks_list.html'
  model = Snacks

class SnacksDetailView(DetailView):
  template_name='snacks_detail.html'
  model = Snacks

class snacksCreateView(CreateView):
  template_name='snacks_create.html'
  model = Snacks
  fields = ['name', 'purchase','description']

class SnacksUpdateView(UpdateView):
  template_name='snacks_update.html'
  model = Snacks
  fields = ['name', 'purchase','description']

class SnacksDeleteView(DeleteView):
  template_name='snacks_delete.html'
  model = Snacks
  success_url = reverse_lazy('snacks_list')



