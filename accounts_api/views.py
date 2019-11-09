from django.shortcuts import render

from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response

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
            return Response({'result':False})
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {'result':True}, status=HTTP_200_OK,
        )

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    print(user)
    if not user:
        return Response({'result':False},
                        status=HTTP_200_OK)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key,
                     'result':True,
                     'user': {
                         'pk': user.id,
                         'ID': user.username,
                         'username':user.last_name,
                        }
                     },
                    status=HTTP_200_OK)

class Logout(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)