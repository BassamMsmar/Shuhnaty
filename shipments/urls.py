from django.urls import path
from .views import  shipments_list
urlpatterns = [
    path('shipments/',shipments_list, name='shipments_list' ),
   
 
]