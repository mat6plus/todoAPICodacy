#from django.shortcuts import render

from rest_framework import generics
from .serializers import TodoSerializers
from .models import Todo

# Create your views here.

class TodoList(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers

class TodoDetails(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers

class TodoCreate(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers

class TodoUpdate(generics.RetrieveUpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers

class TodoDelete(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers
