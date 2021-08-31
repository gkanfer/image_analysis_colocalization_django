import tifffile as tfi
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageEnhance
from numpy import asarray
from skimage.exposure import rescale_intensity,histogram
#from .models import set_intensity,Upload
import pdb
import pandas as pd

def summary_np(array):
    df_describe = pd.DataFrame(array.flatten())
    out=df_describe.describe()
    out=out.astype(int)
    print(out)


def get_image(image):
    pixels = np.array(image)
    #pixels=pixels[50:300,50:300]
    return pixels

def get_image_intensity(image,min_inten,max_inten):
    #breakpoint()
    pixels = np.array(image)
    # if pixels.ndim > 2:
    #     pixels=pixels[:,:,2]
    # else:
    #     pixels=pixels[:,:]
    percentiles = np.percentile(pixels, (int(min_inten), int(max_inten)))
    scaled_ch1 = rescale_intensity(pixels, in_range=tuple(percentiles))
    return scaled_ch1

