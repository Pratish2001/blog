from django.db import models
from cloudinary.models import CloudinaryField
from ckeditor.fields import RichTextField

# Create your models here.
class Blogsite(models.Model):
    title = models.CharField(max_length=200)
    image = CloudinaryField('image')
    description = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    uplode_by = models.CharField(max_length=25)

class Profile(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    user = models.CharField(max_length=255)
    email = models.EmailField()
    profile_pic = CloudinaryField('image')
    about_me = models.TextField()
    
   