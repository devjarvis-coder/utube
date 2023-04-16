import cloudinary
from django.http import HttpResponse
from django.shortcuts import render, redirect
from cloudinary.uploader import upload

from youtube import settings
from .models import Video


# Create your views here.

def index(request):
    return render(request, 'index.html')


def video_upload(request):
    # views.py

    import cloudinary.uploader
    from django.shortcuts import render, HttpResponse
    from .models import Video


def video_upload(request):
    if request.method == 'POST':
        # Get the video file from the request
        video_file = request.FILES.get('video_file')
        # thumbnail = request.FILES['thumbnail']

        # Upload the video file to Cloudinary
        upload_result = cloudinary.uploader.upload(video_file, resource_type='video')

        # Create a new Video object with the uploaded video file's details from Cloudinary
        video = Video(title=request.POST.get('title'),
                      description=request.POST.get('description'),
                      video_file=upload_result['secure_url'])
        video.save()  # Save the Video object to the database

        # Return a response indicating a successful upload
        return HttpResponse('Video uploaded successfully!')
    else:
        # Render the video upload form
        return render(request, 'video_upload.html')

def video_list(request):
    # Retrieve all Video objects from the database
    videos = Video.objects.all()

    # Pass the videos queryset to the template for rendering
    context = {'videos': videos}
    return render(request, 'video_list.html', context)

def player(request,id):
    data = Video.objects.get(id=id)

    return render(request, 'player.html', {'data': data})

# def player(request):
#     videos = Video.objects.all()
#     context = {'videos': videos}
#     return render(request, 'player.html', context)
