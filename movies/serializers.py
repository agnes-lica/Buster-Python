from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Movie, MovieOrder
from users.models import User
from users.serializers import UserSerializer


class MovieSerializer(serializers.Serializer):
    FILM_CLASSIFICATION_CHOICES = (("G", "G"), ("PG", "PG"), ("PG-13", "PG-13"), ("R", "R"), ("NC-17", "NC-17"))
  
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True)
    duration = serializers.CharField(allow_null=True, required=False)
    rating = serializers.ChoiceField(choices=FILM_CLASSIFICATION_CHOICES, default=FILM_CLASSIFICATION_CHOICES[0][1])
    synopsis = serializers.CharField(required=False, allow_null=True)
    added_by = serializers.CharField(read_only=True)
    
    
    
    def create(self, validated_data: dict) -> Movie:
        movie_create = Movie.objects.create(**validated_data)
        return movie_create
    
    
class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    buyed_at = serializers.DateTimeField(read_only=True)
    price = serializers.DecimalField(required=True,max_digits=8, decimal_places=2)
    
    title = serializers.CharField(read_only=True)
    buyed_by = serializers.CharField(read_only=True)
    
    def create(self, validated_data: dict):
        movie_order_create = MovieOrder.objects.create(**validated_data)
        return movie_order_create