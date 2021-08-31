from django.db import models
from .utils import get_image, get_image_intensity
import tifffile as tfi
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
import pdb
import numpy as np
import tifffile as tfi
# Create your models here.
ACTION_CHOICES = (
    ('tif file','tif'),
    ('no tif file','no_tif')
)

class Upload(models.Model):
    image = models.ImageField(upload_to='images')
    title = models.CharField(max_length=200)
    action = models.CharField(max_length=50,choices=ACTION_CHOICES)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    min_inten = models.FloatField(default=1)
    max_inten = models.FloatField(default=76)
    def __str__(self):
        return self.title
        #breakpoint()
    # def __str__(self):
    #     pixels = tfi.imread(self.image)
    #     return np.shape(np.array(pixels))
    def save(self,*args,**kwargs):
        #breakpoint()
        image = Image.open(self.image)
        img = get_image_intensity(image,self.min_inten,self.max_inten)
        im_pil=Image.fromarray(img)
        #save
        buffer = BytesIO()
        im_pil.save(buffer,format='png')
        image_png = buffer.getvalue()
        self.image.save(str(self.image), ContentFile(image_png),save=False)
        #super().save(*args,**kwargs)
        #return self.image_png



# class set_intensity(models.Model):
#     image = models.ImageField(upload_to='images')
#     min_inten = models.FloatField(default=1)
#     max_inten = models.FloatField(default=99)
#     title = models.CharField(max_length=200)
#     def __str__(self):
#         return self.title
#     def save(self,*args,**kwargs):
#         pixels = Image.open(self.image)
#         #pixels = tfi.imread(self.image)
#         pixels = np.array(pixels)
#         if pixels.ndim > 2:
#             pixels=pixels[:,:,0]
#         else:
#             pixels=pixels[:,:]
#         img = get_image_intensity(pixels,self.max_inten,self.max_inten)
#         im_pil=Image.fromarray(img)
#         #save
#         buffer = BytesIO()
#         im_pil.save(buffer,format='png')
#         image_png = buffer.getvalue()
#         self.image.save(str(self.image), ContentFile(image_png),save=False)
#         super().save(*args,**kwargs)
#         #return self.image_png



