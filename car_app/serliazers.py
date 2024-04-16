# move_app/serializers.py
from rest_framework import serializers
from .models import Car
from car_model_app.serliazers import CarModelSerializer

class CarSerializer(serializers.ModelSerializer):
    
    car_model = CarModelSerializer()

    class Meta:

        model = Car

        fields = ('id', 'car_model' 'number_of_owners', 'manufacture_year', 'number_of_doors', 'mileage')
    