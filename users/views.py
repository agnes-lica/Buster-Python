from django.contrib.auth import authenticate
from rest_framework.views import APIView, Request, Response, status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import UserSerializer, LoginSerializer
from .models import User


class RegisterView(APIView):
    def get(self, request: Request) -> Response:
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)  # type: ignore
        serializer.is_valid(raise_exception=True)

        entered_username = request.data["username"]
        validated_username = User.objects.filter(username=entered_username).exists()
        
        entered_email = request.data["email"]
        validated_email = User.objects.filter(email=entered_email).exists()
        
        if validated_username and validated_email:
            return Response({"username" : ["username already taken."], "email" : ["email already registered."]}, status.HTTP_400_BAD_REQUEST)
        elif validated_email:
            return Response({"email" : ["email already registered."]}, status.HTTP_400_BAD_REQUEST)
        elif validated_username:
            return Response({"username" : ["username already taken."]}, status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

class LoginView(TokenObtainPairView):
    def post(self, request: Request) -> Response:
        serializer = LoginSerializer(data=request.data)  # type: ignore
        serializer.is_valid(raise_exception=True)

        user = authenticate(username=serializer.validated_data["username"], password=serializer.validated_data["password"])
        
        if not user:
            return Response({"detail" : "No active account found with the given credentials"}, status.HTTP_401_UNAUTHORIZED)
        
        
        refresh = RefreshToken.for_user(user)
        token = {"refresh": str(refresh), "access": str(refresh.access_token)}        
        return Response(token, status.HTTP_200_OK)