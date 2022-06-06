from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *

# Create your views here.

class ListTodo(generics.ListAPIView): #view todo data
    queryset=Todo.objects.all()
    serializer_class=TodoSerializer

class CreateTode(generics.CreateAPIView): #create 
    queryset=Todo.objects.all()
    serializer_class=TodoSerializer

class DetailTodo(generics.RetrieveUpdateAPIView): #update
    queryset=Todo.objects.all()
    serializer_class=TodoSerializer

class DeleteTodo(generics.DestroyAPIView): #delete
    queryset=Todo.objects.all()
    serializer_class=TodoSerializer

