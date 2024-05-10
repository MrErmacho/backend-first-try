from django.shortcuts import render
from .models import *

# Create your views here.
def playlist(request):
    Videos = Video.objects.all
    return render(request, 'playlist/playlist.html', {
        'Videos': Videos
    })

def video_uploader(request):
    if request.method == "Post":
        Video.objects.create (
            title = request.POST['title'],
            embed = request.POST['embed']
        )
    return render(request, 'playlist/video_uploader.html')
