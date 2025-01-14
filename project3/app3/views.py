from django.shortcuts import render
from .models import Todo3

# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy

class TodoList(ListView):
  model=Todo3
  context_object_name='Todos'

class TodoDetails(DetailView):
  model=Todo3
  context_object_name='todo'

class TodoCreate(CreateView):
  model=Todo3
  fields='__all__'
  success_url=reverse_lazy('Todos')

class TodoUpdate(UpdateView):
  model=Todo3
  fields='__all__'
  success_url=reverse_lazy('Todos')

class TodoDelete(DeleteView):
   model=Todo3
   fields='__all__'
   success_url=reverse_lazy('Todos')
   context_object_name='todooo'



   