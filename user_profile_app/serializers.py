from rest_framework import serializers
from app_user_app.models import AppUser
from .models import UserProfile
from app_user_app.serializers import AppUserSerializer

class UserProfileSerializer(serializers.ModelSerializer):

    account = AppUserSerializer(many=False)
    class Meta:
        model = UserProfile
        fields = ('account','street_name', 'street_number', 'zip_code', 'city')