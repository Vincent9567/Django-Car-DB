# move_app/serializers.py
from rest_framework import serializers
from .models import CarModel


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id','make', 'model')