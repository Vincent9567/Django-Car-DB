from django.urls import path, register_converter
# Explicit imports
from .views import AllCarModels
# Remember all urls are prefaced by http://localhost:8000/api/v1/carmodels/


urlpatterns = [
    # Currently only takes GET requests
    path('', AllCarModels.as_view(), name='all_cars'),
]