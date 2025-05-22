# devices/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Device
from .forms import DeviceForm

@login_required
def device_list(request):
    devices = request.user.devices.all()
    return render(request, 'devices/device_list.html', {'devices': devices})

@login_required
def device_create(request):
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            device = form.save(commit=False)
            device.user = request.user
            device.save()
            return redirect('device_list')
    else:
        form = DeviceForm()
    return render(request, 'devices/device_form.html', {'form': form})

@login_required
def device_update(request, pk):
    device = get_object_or_404(Device, pk=pk, user=request.user)
    if request.method == 'POST':
        form = DeviceForm(request.POST, instance=device)
        if form.is_valid():
            form.save()
            return redirect('device_list')
    else:
        form = DeviceForm(instance=device)
    return render(request, 'devices/device_form.html', {'form': form})

@login_required
def device_delete(request, pk):
    device = get_object_or_404(Device, pk=pk, user=request.user)
    if request.method == 'POST':
        device.delete()
        return redirect('device_list')
    return render(request, 'devices/device_confirm_delete.html', {'device': device})
