from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status

from .serializers import UserSerializer


class RegisterView(APIView):
    def get(self, request: Request) -> Response:
        return Response("")

    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)  # type: ignore
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)
