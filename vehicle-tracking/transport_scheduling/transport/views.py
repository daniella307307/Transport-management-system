from django.shortcuts import render, redirect, get_object_or_404
from .models import Vehicle, Driver, Schedule, Route
from .forms import VehicleForm, DriverForm, ScheduleForm, RouteForm

# Vehicle Views

def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'transport/vehicle_list.html', {'vehicles': vehicles})

def add_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
    else:
        form = VehicleForm()
    return render(request, 'transport/add_vehicle.html', {'form': form})

def edit_vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    if request.method == 'POST':
        form = VehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
    else:
        form = VehicleForm(instance=vehicle)
    return render(request, 'transport/edit_vehicle.html', {'form': form, 'vehicle': vehicle})

def delete_vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    vehicle.delete()
    return redirect('vehicle_list')

# Driver Views

def driver_list(request):
    drivers = Driver.objects.all()
    return render(request, 'transport/driver_list.html', {'drivers': drivers})

def add_driver(request):
    if request.method == 'POST':
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('driver_list')
    else:
        form = DriverForm()
    return render(request, 'transport/add_driver.html', {'form': form})

def edit_driver(request, driver_id):
    driver = get_object_or_404(Driver, id=driver_id)
    if request.method == 'POST':
        form = DriverForm(request.POST, instance=driver)
        if form.is_valid():
            form.save()
            return redirect('driver_list')
    else:
        form = DriverForm(instance=driver)
    return render(request, 'transport/edit_driver.html', {'form': form, 'driver': driver})

def delete_driver(request, driver_id):
    driver = get_object_or_404(Driver, id=driver_id)
    driver.delete()
    return redirect('driver_list')

# Route Views

def route_list(request):
    routes = Route.objects.all()
    return render(request, 'transport/route_list.html', {'routes': routes})

def add_route(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('route_list')
    else:
        form = RouteForm()
    return render(request, 'transport/add_route.html', {'form': form})

def edit_route(request, route_id):
    route = get_object_or_404(Route, id=route_id)
    if request.method == 'POST':
        form = RouteForm(request.POST, instance=route)
        if form.is_valid():
            form.save()
            return redirect('route_list')
    else:
        form = RouteForm(instance=route)
    return render(request, 'transport/edit_route.html', {'form': form, 'route': route})

def delete_route(request, route_id):
    route = get_object_or_404(Route, id=route_id)
    route.delete()
    return redirect('route_list')

# Schedule Views

def schedule_list(request):
    schedules = Schedule.objects.all()
    return render(request, 'transport/schedule_list.html', {'schedules': schedules})

def add_schedule(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('schedule_list')
    else:
        form = ScheduleForm()
    return render(request, 'transport/add_schedule.html', {'form': form})

def edit_schedule(request, schedule_id):
    schedule = get_object_or_404(Schedule, id=schedule_id)
    if request.method == 'POST':
        form = ScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            return redirect('schedule_list')
    else:
        form = ScheduleForm(instance=schedule)
    return render(request, 'transport/edit_schedule.html', {'form': form, 'schedule': schedule})

def delete_schedule(request, schedule_id):
    schedule = get_object_or_404(Schedule, id=schedule_id)
    schedule.delete()
    return redirect('schedule_list')

def dashboard(request):
    return render(request, 'transport/dashboard.html')