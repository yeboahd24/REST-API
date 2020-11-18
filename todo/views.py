from django.shortcuts import render
from .models import Todo
from .serializers import TodoSerializer
from rest_framework import generics, permissions # new
from .permissions import IsAuthorOrReadOnly # new


class ListTodo(generics.ListAPIView):
    # permission_classes = (permissions.IsAuthenticated,) # new
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,) # new
    permission_classes = (IsAuthorOrReadOnly,) # new custome
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

