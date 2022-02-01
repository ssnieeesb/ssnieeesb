from datetime import date, datetime
from django.shortcuts import render, get_object_or_404
from .models import events
from .models import gallery
import requests
import os
from home.updater import changer
# Create your views here.
global_wrapper=''
def index(request):
    file='index.html'
    changer(file)
    event = list(events.objects.filter(start_date__gte=datetime.now()).order_by('start_date')[:5])
    return render(request,global_wrapper+file, {'events': event})

def about(request):
    file='about.html'
    changer(file)
    return render(request,global_wrapper+file, {'events' : events.objects.all()})

def past_events(request):
    file='past_events.html'
    changer(file)
    event = events.objects.filter(start_date__lt = datetime.now()).order_by('-start_date')
    return render(request,global_wrapper+file, {'events' : event})

def upcoming_events(request):
    file='upcoming_events.html'
    changer(file)
    event = events.objects.filter(start_date__gte = datetime.now()).order_by('start_date')
    return render(request,global_wrapper+file, {'events' : event})

def contact(request):
    file='contact.html'
    changer(file)
    return render(request,global_wrapper+file)

def gallery_images(request):
    file='gallery.html'
    changer(file)
    return render(request,global_wrapper+file, {'images':gallery.objects.all()})

def event_page_base(request, event_id):
    file='event_page_base.html'
    changer(file)
    event = get_object_or_404(events, pk=event_id)
    return render(request, global_wrapper+file, {'events':event})

def base(request):
    file='base.html'
    changer(file)
    return render(request,"Page not found error!!")
