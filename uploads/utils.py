import tifffile as tfi
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageEnhance
from numpy import asarray
from skimage.exposure import rescale_intensity,histogram
#from .models import set_intensity,Upload

def get_image(image):
    pixels = np.array(image)
    #pixels=pixels[50:300,50:300]
    return pixels

def get_image_intensity(image,min_inten,max_inten):
    #image = np.array(image)
    #percentiles = np.percentile(image, (1, 89))
    percentiles = np.percentile(image, min_inten, max_inten)
    scaled_ch1 = rescale_intensity(image, in_range=tuple(percentiles))
    return scaled_ch1

