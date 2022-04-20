from django.db import models
import datetime
import os

# Create your models here.
def filepath(request, filename):
    old_filename= filename
    timeNow= datetime.datetime.now().strftime('%y%m%d%H:%M:%S')
    filename= '%s%s' % (timeNow, old_filename)
    return os.path.join('uploads/', filename)



class Image(models.Model):
    name= models.TextField(max_length=100)
    description= models.TextField(max_length=400)
    image= models.ImageField(upload_to=filepath, null=True, blank=True)