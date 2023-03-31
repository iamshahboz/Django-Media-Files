from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from . serializers import DogSerializer
from . models import Dog

# Create your views here.

def homepage(request):
    return HttpResponse("This is your application")

class DogListCreate(APIView):
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self,request):
        dogs = Dog.objects.all()
        serializer = DogSerializer(dogs,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = DogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class DogDetail(APIView):
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self,request,pk):
        dog = get_object_or_404(Dog,pk=pk)
        serializer = DogSerializer(dog)
        return Response(serializer.data)
    
    def put(self,request,pk):
        dog = get_object_or_404(Dog,pk=pk)
        serializer = DogSerializer(dog,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk):
        dog = get_object_or_404(Dog,pk=pk)
        serializer = DogSerializer(dog,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        dog = get_object_or_404(Dog,pk=pk)
        dog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

    





