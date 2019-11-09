from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import generics

from rest_framework.decorators import api_view

from rest_framework.response import Response

# from rest_framework.filters import SearchFilter

from .models import Province
from .models import Borough

from .serializer import ProvinceSerializer
from .serializer import BoroughSerializer

from rest_framework.filters import BaseFilterBackend

class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer

class BoroughViewSet(viewsets.ModelViewSet):
    queryset = Borough.objects.all()
    serializer_class = BoroughSerializer

# class BoroughList(ListAPIView):
#     serializer_class = BoroughSerializer

#     class Meta:
#         model = Borough

#     def get_queryset(self):
#         qs = super().get_queryset()
#         search = self.request.query_params.get('province',)
#         if search:
#             qs = qs.filter(province_code=int(search))
#         print(province_code)
#         return qs

# class BoroughList(generics.ListAPIView):
#     def get_queryset(self):
#         return Borough.objects.filter(province_code=self.request.data('province'))

# @api_view(["GET"])
# def BoroughList(request):
#     print(request.GET['province'])
#     boroughs = Borough.objects.filter(province_code=request.GET['province'])

#     return Response({'boroughs': boroughs})

class BoroughList(generics.ListAPIView):
    serializer_class = BoroughSerializer
    def get_queryset(self):
        qs = Borough.objets.filter(province_code=request.get.date('province'))
        return qs