from django.urls import path
from .views import *

urlpatterns =[
    path('', home, name='home'),
    path('registers/', registerattempt, name='registers'),
    path('logins/', loginattempt, name='logins'),
    path('logouts/', logoutattempt,name='logoutattempt'),
    path('rent-booking', rental, name='rental'),
    path('customerlist', customerlist, name='customerlist'),
    path('rentallist', rentallist, name='rentallist'),
    path('vehiclesavailable', vehiclesavailable, name='vehiclesavailable'),
]