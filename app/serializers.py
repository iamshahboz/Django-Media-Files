from rest_framework import serializers
from . models import Dog,Book,Author

class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ['id','name','image']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book 
        fields = ['id','name','price','number_in_stock','genre','author']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id','name']
        
    
        