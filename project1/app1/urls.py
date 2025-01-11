from django.urls import path
from .views import TaskList1,DetailList,CreateList,UpdateList,DeleteList,CustomeLogin
from django.contrib.auth.views import LogoutView

urlpatterns=[
  path('login/',CustomeLogin.as_view(), name='login'),
  path('logout/',LogoutView.as_view(next_page='login'), name='logout'),
  path('',TaskList1.as_view(),name='Tasks'),
  
  path('task/<int:pk>',DetailList.as_view(), name='task'),
  path('create/',CreateList.as_view(),name='create'),
  path('update/<int:pk>',UpdateList.as_view(),name='update'),
  path('delete/<int:pk>', DeleteList.as_view(),name='delete')
]