from django.db import models

# Create your models here.


class Image_Uploader(models.Model):
    image = models.ImageField(upload_to='app/static/asset/Image_Folder')
