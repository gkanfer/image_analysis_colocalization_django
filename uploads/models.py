from django.db import models
from .utils import get_image
import tifffile as tfi
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
import pdb
import numpy as np
# Create your models here.
ACTION_CHOICES = (
    ('No_Filter','no filter'),
    ('Chose_Intensity','Intensity')
)

class Upload(models.Model):
    image = models.ImageField(upload_to='images')
    title = models.CharField(max_length=200)
    action = models.CharField(max_length=50,choices=ACTION_CHOICES)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    def save(self,*args,**kwargs):
        #open image
        pixels = Image.open(self.image)
        #breakpoint()
        #pixels = tfi.imread(self.image)
        pixels = np.array(pixels)
        pixels=pixels[:,:,:]
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



