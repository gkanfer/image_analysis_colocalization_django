import tifffile as tfi
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageEnhance
from numpy import asarray
from skimage.exposure import rescale_intensity,histogram


def get_image(image):
    pixels = np.array(image)
    pixels=pixels[50:300,50:300,:]
    return pixels




# def get_image(image,action):
#     #image = np.array(image)
#     if action=='Chose_Intensity':
#         percentiles = np.percentile(image, (1, 89))
#         scaled_ch1 = rescale_intensity(image, in_range=tuple(percentiles))
#     elif action=='No_Filter':
#         scaled_ch1 = image
#     return scaled_ch1

