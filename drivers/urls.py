from django.urls import path
from .views import driver_list, add_driver

urlpatterns = [
    path('deivers/',driver_list, name='driver_list' ),
    path('deivers/add',add_driver, name='add_driver' )
]