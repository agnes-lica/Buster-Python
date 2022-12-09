from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication

from users.permissions import IsAdminOrReadOnly
from .serializers import MovieSerializer
from .models import Movie


class MovieView(APIView):
  
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]
  
    def get(self, request: Request) -> Response: #livre
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request: Request) -> Response: #employee
        serializer = MovieSerializer(data=request.data)  # type: ignore
        serializer.is_valid(raise_exception=True)

        serializer.save(user=request.user, added_by=request.user.email)

        return Response(serializer.data, status.HTTP_201_CREATED)

class MovieIdView(APIView):
  
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    
    def get(self, request: Request, movie_id: int) -> Response: #livre
       movie = get_object_or_404(Movie, id=movie_id)
       
       serializer = MovieSerializer(movie)
       
       return Response(serializer.data, status.HTTP_200_OK)
     
    def delete(self, request: Request, movie_id: int) -> Response: #employee
       movie = get_object_or_404(Movie, id=movie_id)
       movie.delete()
       
       return Response(status=status.HTTP_204_NO_CONTENT)
