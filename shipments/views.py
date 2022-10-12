from django.shortcuts import render
from .models import AddShipmentModel

# Create your views here.
def shipments_list(request):
    shipmens = AddShipmentModel.objects.all()

    return render(request, 'shipments/shipments-list.html',{'shipmens':shipmens})