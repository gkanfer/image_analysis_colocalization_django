import tifffile as tfi
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageEnhance
#from PIL import fromarray
from numpy import asarray
from skimage import data,io
from skimage.exposure import rescale_intensity,histogram
import os
import glob

imgae_path = "/Users/kanferg/Desktop/NIH_Youle/Python_projacts_general/django_app/Images_example/"
image_name=glob.glob("*.tiff")