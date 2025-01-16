from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Todo4
# Create your views here.


class TodoList(ListView):
  model=Todo4
  context_object_name='TodoTask'
  