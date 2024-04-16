from django.shortcuts import render
from rest_framework.views import APIView, Response
from .serliazers import UserPorfileSerializer

class AppUser(APIView):
    def get(self, request):
        user = AppUser.objects.order_by('first_name')
        serializer = AppUserSerializer(user)
        return Response(serializer.data)