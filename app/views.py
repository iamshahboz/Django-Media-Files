from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from rest_framework import generics
from . serializers import DogSerializer
from . models import Dog

# Create your views here.

def homepage(request):
    return HttpResponse("This is your application")

class DogListCreate(generics.ListCreateAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

class DogAction(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

    





