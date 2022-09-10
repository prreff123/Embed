from django.shortcuts import render
from django.http import HttpResponse
from .models import Video
# Create your views here.

def index(request):
    videos = Video.objects.all()
    return render(request, 'index.html', context={'videos': videos})