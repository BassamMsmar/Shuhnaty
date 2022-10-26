from django.shortcuts import get_object_or_404, redirect, render

from .forms import shipmentsForm
from .models import ShipmentModel


# Create your views here.
def shipments_list(request):
    shipmens = ShipmentModel.objects.all()
    context = {
        'shipmens':shipmens,
    }
    return render(request, 'shipments/shipments-list.html',context)


def shipments_details(request, pk):
    shipment = get_object_or_404(ShipmentModel ,pk=pk)

    return render(request, 'shipments/shipments-details.html',{'shipment':shipment})


def shipments_delete(request, pk):
    shipmens = ShipmentModel.objects.get(pk=pk)
    shipmens.delete()
    return redirect('shipments_list')


def shipments_add(request):
    if request.method == 'POST':
        form = shipmentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shipments_list')
    else:
         form = shipmentsForm()

    return render(request, 'shipments/shipments-add.html',{'form':form})


def shipments_edit(request, pk):
    shipmens = ShipmentModel.objects.get(pk=pk)
    if request.method == 'POST':
        form = shipmentsForm(request.POST, instance=shipmens)
        if form.is_valid():
            form.save()
            return redirect('shipments_list')
    else:
         form = shipmentsForm(instance=shipmens)

    return render(request, 'shipments/shipments-add.html',{'form':form})
