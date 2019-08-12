from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo 
# Create your views here.
context = {
        'obj' : Photo.objects.all().order_by('-id'),
       
    }

def home_view(request, *args, **kwargs):
    return render(request, "home.html",context)

def photo_view(request, *args, **kwargs):
    return render(request, "photo.html",context)

