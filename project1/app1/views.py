from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import Task1


class CustomeLogin(LoginView):
  template_name='app1/login.html'
  fields='__all__'
  redirect_authenticated_user=True

  def get_success_url(self):
    return reverse_lazy('Tasks')


class TaskList1(ListView):
  model=Task1
  context_object_name='Tasks'

class DetailList(DetailView):
  model=Task1
  context_object_name='task'

class CreateList(CreateView):
  model=Task1
  fields='__all__'
  success_url=reverse_lazy('Tasks')

class UpdateList(UpdateView):
  model=Task1
  fields='__all__'
  success_url=reverse_lazy('Tasks')

class DeleteList(DeleteView):
  model=Task1
  fields='__all__'
  context_object_name='taskii'
  success_url=reverse_lazy('Tasks')
  




