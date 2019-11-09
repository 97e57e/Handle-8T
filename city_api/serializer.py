from rest_framework import serializers

from .models import Province
from .models import Borough

class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields ='__all__'

class BoroughSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borough
        fields='__all__'