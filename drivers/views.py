from django.shortcuts import render
from .models import AddDriverModel

# Create your views here.
def driver_list(request):
    drivers = AddDriverModel.objects.all()

    return render(request, 'drivers/driver-list.html',{'drivers':drivers})