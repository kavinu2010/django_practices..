from django.urls import path
from .views import TodoList,TodoDetails,TodoCreate,TodoUpdate,TodoDelete

urlpatterns=[
  path('',TodoList.as_view(), name='Todos' ),
  path('todo/<int:pk>/',TodoDetails.as_view(), name='todo' ),
  path('create/',TodoCreate.as_view(), name='create' ),
  path('update/<int:pk>/',TodoUpdate.as_view(), name='update' ),
  path('delete/<int:pk>/',TodoDelete.as_view(), name='delete' ),
  

]