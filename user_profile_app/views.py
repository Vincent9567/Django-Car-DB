from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers import serialize
from rest_framework.views import APIView, Response
from rest_framework import status
from .models import UserProfile
from .serializers import UserProfileSerializer

class AllUserProfiles(APIView):
    
    def get(self, request):
        user_profiles = UserProfile.objects.order_by('pk')
        serializer = UserProfileSerializer(app_users, many=True)  
        return Response(serializer.data)
    
    def post(self, request, response):
        serializer = UserProfileSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_BAD_REQUEST)
    

class SelectUserProfiles(APIView):

    def get_user_profile(self, id):
        if isinstance(id, int):
            return UserProfile.objects.get(id=id)
        else:
            return UserProfile.objects.get(first_name=id)

    def get(self, request, id):
        user_profile = self.get_app_user(id)
        json_user_profile = serialize('json', ['user_profile'])
        user_profile_serialized = json.loads(json_user_profile)
        return Response(user_profile_serialized.data)
    

    def delete(self, request, id):
        pass
        user_profile = self.get_user_profile(id)
        serialized_