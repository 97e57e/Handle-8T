from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView

from .models import Province
from .models import Borough

from .serializer import ProvinceSerializer
from .serializer import BoroughSerializer

class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer