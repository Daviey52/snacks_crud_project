from django.shortcuts import render
from .models import Snacks

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

class SnacksUpdateView(UpdateView):
  template_name='snacks_update.html'
  model = Snacks

class SnacksDeleteView(DeleteView):
  template_name='snacks_delete.html'
  model = Snacks


