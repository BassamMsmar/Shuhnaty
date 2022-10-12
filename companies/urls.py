from django.urls import path
from .views import  company_list, add_company

urlpatterns = [
    path('companies/',company_list, name='company_list' ),
    path('companies/add/',add_company, name='add_company' ),
 
]