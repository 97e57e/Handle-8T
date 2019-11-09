from django.shortcuts import render

from rest_framework import views
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView

from .serializer import CreateUserSerializer
from .serializer import LoginSerializer

from django.contrib.auth.models import User

from django.views.decorators.csrf import ensure_csrf_cookie

class RegistrationAPI(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    def get(self, request, format=None):
        return Response("test")

    def post(self, request, *args, **kwargs):
        if len(request.data["username"]) < 6 or len(request.data["password"]) < 4:
            body = {"message": "short field"}
            return Response(body, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        profile_serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
            }
        )

@ensure_csrf_cookie
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
            }
        )

class Logout(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)