from django.urls import path, register_converter
from . import views
from .views import AllAdverts, SelectedAdvert
from .converters import IntOrStrConverter

register_converter(IntOrStrConverter, 'int_or_string')


urlpatterns = [
    path('advertisement/', views.advertisement_response)
]

from .views import Advertisements
# Remember all urls are prefaced by http://localhost:8000/api/v1/cars/


urlpatterns = [
    # Currently only takes GET requests
    path('', Advertisements.as_view(), name='all_advertisements'),
    path('<int_or_str:id>/', SelectedAdvert.as_view(), name = 'selected_advert')
]