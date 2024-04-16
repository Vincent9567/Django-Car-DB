from rest_framework import serializers
from .models import UserProfile

class UserPorfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('street_name', 'street_number', 'zip_code', 'city')