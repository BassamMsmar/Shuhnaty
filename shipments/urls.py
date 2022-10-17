from django.urls import path
from .views import  shipments_list, shipments_add, shipments_details, shipments_delete, shipments_edit
urlpatterns = [
    path('shipments/',shipments_list, name='shipments_list' ),
    path('shipments/add/',shipments_add, name='shipments_add' ),
    path('shipments/delete/<int:pk>',shipments_delete, name='shipments_delete' ),
    path('shipments/edit/<int:pk>',shipments_edit, name='shipments_edit' ),
    path('shipments/details/<int:pk>',shipments_details, name='shipments_details' ),
   
 
]