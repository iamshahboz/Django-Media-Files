from rest_framework import serializers
from . models import Dog

class DogSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Dog
        fields = ['id','name','image']
        