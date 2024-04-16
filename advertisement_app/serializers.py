# move_app/serializers.py
from rest_framework import serializers
from .models import Advertisement
from car_app.serliazers import CarSerializer
from app_user_app.serliazers import AppUserSerializer

class AdvertisementSerializer(serializers.ModelSerializer):
    

    car_id = CarSerializer()
    seller_account_id = AppUserSerializer()

    class Meta:

        model = Advertisement
        fields = ('advertisement_date', 'seller_account_id', 'car_id')