from django.urls import path, register_converter
# Explicit imports
from .views import AllCars
# Remember all urls are prefaced by http://localhost:8000/api/v1/cars/


urlpatterns = [
    # Currently only takes GET requests
    path('', AllCars.as_view(), name='all_cars'),
]