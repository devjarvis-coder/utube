from cloudinary.models import CloudinaryField
from django.db import models


# Create your models here.
class youtube(models.Model):
    vtitle = models.CharField(max_length=255)
    vdesc = models.TextField()
    video = CloudinaryField('image')


class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    thumbnail = CloudinaryField('image')
    video_file = CloudinaryField(resource_type='video')
    upload_date = models.DateTimeField(auto_now_add=True)
