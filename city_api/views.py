from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from rest_framework.filters import SearchFilter

from .models import Province
from .models import Borough

from .serializer import ProvinceSerializer
from .serializer import BoroughSerializer

class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer

class BoroughViewSet(viewsets.ModelViewSet):
    queryset = Borough.objects.all()
    serializer_class = BoroughSerializer
    filter_backends = ()

class BoroughList(ListAPIView):
    serializer_class = BoroughSerializer

    class Meta:
        model = Borough

    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.query_params.get('province',)
        if search:
            qs = qs.filter(province_code=int(search))
        print(province_code)
        return qs
