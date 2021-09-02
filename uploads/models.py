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


class Upload(models.Model):
    #defult_image1='/images/1_.tif'
    image = models.ImageField(upload_to='images')
    title = models.CharField(max_length=200,default='Ch1')
    min_inten = models.FloatField(default=1)
    max_inten = models.FloatField(default=76)
    def __str__(self):
        return str(self.id)
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
        super().save(*args,**kwargs)
        #return self.image_png



class test_model(models.Model):    
    #defult_image2='/images/0_.tif'
    image_2 = models.ImageField(upload_to='images')
    title_2 = models.CharField(max_length=200,default='Ch2')
    min_inten_2 = models.FloatField(default=1)
    max_inten_2 = models.FloatField(default=76)
    def __str__(self):
        return str(self.id)
        #breakpoint()
    # def __str__(self):
    #     pixels = tfi.imread(self.image)
    #     return np.shape(np.array(pixels))
    def save(self,*args,**kwargs):
        #breakpoint()
        image_2 = Image.open(self.image_2)
        img = get_image_intensity(image_2,self.min_inten_2,self.max_inten_2)
        im_pil=Image.fromarray(img)
        #save
        buffer = BytesIO()
        im_pil.save(buffer,format='png')
        image_png = buffer.getvalue()
        self.image_2.save(str(self.image_2), ContentFile(image_png),save=False)
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



