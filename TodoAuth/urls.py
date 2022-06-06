import imp
from django.urls import path
from .views import *

urlpatterns = [
    path('',ListTodo.as_view()), #View all data
    path('add',CreateTode.as_view()), #create todo list
    path('update/<int:pk>',DetailTodo.as_view()), # update particular todo list
    path('delete/<int:pk>',DeleteTodo.as_view()) #delete todo list
]
