from django.shortcuts import render,HttpResponseRedirect
from .forms import ImageForm,ImageForm_2
from .utils import get_image, get_image_intensity
from .models import Upload, test_model
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageEnhance
from numpy import asarray
import pdb


def home(request):
    return render(request,'home.html',{})

def Protein_interaction(request):
    """Process images uploaded by users"""
    #breakpoint()
    if request.method == 'POST':
        #breakpoint()
        ImageForm_form = ImageForm(request.POST, request.FILES)
        ImageForm2_from = ImageForm_2(request.POST, request.FILES)
        if ImageForm_form.is_valid():
            img_obj = ImageForm_form.instance
            return render(request, 'Protein_interaction.html', {'ImageForm_form': ImageForm_form, 'img_obj': img_obj})
        if ImageForm2_from.is_valid():
            img_obj_2 = ImageForm2_from.instance
            return render(request, 'Protein_interaction.html', {'ImageForm2_from': ImageForm2_from,'img_obj_2': img_obj_2})

    else:
        ImageForm_form = ImageForm()
        ImageForm2_from = ImageForm_2()
    return render(request, 'Protein_interaction.html', {'ImageForm_form': ImageForm_form,'ImageForm2_from':ImageForm2_from})




# def Protein_interaction(request):
#     """Process images uploaded by users"""
#     #breakpoint()
#     if request.method == 'POST':
#         form = ImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             img_obj = form.instance
#             return render(request, 'Protein_interaction.html', {'form': form, 'img_obj': img_obj})

#     else:
#         form = ImageForm()
#     return render(request, 'Protein_interaction.html', {'form': form})



def image_process(request):
    """Process images uploaded by users"""
    pass
    # breakpoint()
    # if request.method == 'POST':
    #     form2 = ImageForm_2(request.POST, request.FILES)
    #     if form2.is_valid():
    #         form2.save()
    #         # Get the current instance object to display in the template
    #         img_obj2 = form2.instance
    #         return render(request, 'Protein_interaction.html', {'form2': form2, 'img_obj2': img_obj2})
    # else:
    #     form2 = ImageForm_2()
    # return render(request, 'Protein_interaction.html', {'form2': form2})


# def Protein_interaction(request):
#     return render(request,'Protein_interaction.html',{})

def Image_segmentation(resquset):
    return render(resquset,'Image_segmentation.html',{})

def SMLM(resquset):
    return render(resquset,'SMLM.html',{})

def Deep_learning(resquset):
    return render(resquset,'Deep_learning.html',{})

def Genomic_screen(resquset):
    return render(resquset,'Genomic_screen.html',{})