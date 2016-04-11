from django.shortcuts import render
from .models import Shot
from .forms import ShotForm
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.utils import timezone


# Create your views here.

def shots_list(request):
    shots = Shot.objects.order_by('-registered_date')
    return render(request, 'shots_list.html', {'shots': shots})

def shots_map(request):
    shots = Shot.objects.order_by('-registered_date')
    center = Shot.objects.order_by('-registered_date')[0]
    return render(request, 'shots_map.html', {'shots': shots, 'center': center})

def shot_new(request):
    if request.method == "POST":
        form = ShotForm(request.POST)
        if form.is_valid():
            shot = form.save(commit=False)
            shot.registered_date = timezone.now()
            shot.save()
            return redirect('/')
    else:
        form = ShotForm
    return render(request, 'commander/shot_new.html', {'form': form})

def shot_new_get(request, iot_id, lat, longt, elev, head):
    form = ShotForm(request.GET)
    shot = form.save(commit=False)
    shot.IOT_id = iot_id
    shot.gps_lat = lat
    shot.gps_long = longt
    shot.registered_date = timezone.now()
    shot.gps_elev = elev
    shot.heading_point = head
    shot.save()
    return redirect('/')
