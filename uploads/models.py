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
    def __str__(self):
        return self.title
        #breakpoint()
    # def __str__(self):
    #     pixels = tfi.imread(self.image)
    #     return np.shape(np.array(pixels))
    def save(self,*args,**kwargs):
        #open image
        #breakpoint()
        if self.action=='tif':
            pixels = tfi.imread(self.image)
        else:
            pixels = Image.open(self.image)
        #pixels = tfi.imread(self.image)
        pixels = np.array(pixels)
        pixels=pixels[:,:,0]
        #pixels = pixels[0,:,:]
        #use the normalisation method
        img = get_image(pixels)
        im_pil=Image.fromarray(img)
        #save
        buffer = BytesIO()
        im_pil.save(buffer,format='png')
        image_png = buffer.getvalue()
        self.image.save(str(self.image), ContentFile(image_png),save=False)
        super().save(*args,**kwargs)
        #return self.image_png

class set_intensity(models.Model):
    image = models.ImageField(upload_to='images')
    min_inten = models.CharField(max_length=5)
    max_inten = models.CharField(max_length=5)
    number_of_image_channels = models.CharField(max_length=5)
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title
    def save(self,*args,**kwargs):
        #open image
        if self.action=='tif':
            pixels = tfi.imread(self.image)
        else:
            pixels = Image.open(self.image)
        #breakpoint()
        #pixels = tfi.imread(self.image)
        pixels = np.array(pixels)
        pixels=pixels[:,:,int(self.number_of_image_channels)]
        #pixels = pixels[0,:,:]
        #use the normalisation method
        img = get_image_intensity(pixels,self.max_inten,self.max_inten)
        im_pil=Image.fromarray(img)
        #save
        buffer = BytesIO()
        im_pil.save(buffer,format='png')
        image_png = buffer.getvalue()
        self.image.save(str(self.image), ContentFile(image_png),save=False)
        super().save(*args,**kwargs)
        #return self.image_png



