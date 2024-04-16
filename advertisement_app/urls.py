from django.urls import path
from . import views

urlpatterns = [
    path('advertisement/', views.advertisement_response)
]

from .views import Advertisements
# Remember all urls are prefaced by http://localhost:8000/api/v1/cars/


urlpatterns = [
    # Currently only takes GET requests
    path('', Advertisements.as_view(), name='all_advertisements'),
]