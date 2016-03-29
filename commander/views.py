from django.shortcuts import render
from .models import Shot
# Create your views here.

def shots_list(request):
    shots = Shot.objects.order_by('-registered_date')
    return render(request, 'shots_list.html', {'shots': shots})

def shots_map(request):
    shots = Shot.objects.order_by('-registered_date')
    center = Shot.objects.order_by('-registered_date')[0]
    return render(request, 'shots_map.html', {'shots': shots, 'center': center})


