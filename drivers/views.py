from django.shortcuts import render, redirect
from .models import AddDriverModel
from .forms import AddDriverForm

# Create your views here.
def driver_list(request):
    drivers = AddDriverModel.objects.all()
    return render(request, 'drivers/driver-list.html',{'drivers':drivers})

def add_driver(request):
    if request.method == 'POST':
        driver_form = AddDriverForm(request.POST, request.FILES)
        if driver_form.is_valid():
            driver_form.save()
            return redirect('driver_list')
    else:
        driver_form = AddDriverForm()

    return render(request, 'drivers/driver-add_edit.html',{'driver_form':driver_form})
    