from django.shortcuts import render
from .forms import ImageForm, ImageForm_process
from .utils import get_image, get_image_intensity
from .models import Upload
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageEnhance
from numpy import asarray
import pdb
from django.core.files.storage import FileSystemStorage


def home(request):
    return render(request,'home.html',{})

def Protein_interaction(request):
    """Process images uploaded by users"""
    #breakpoint()
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        form_process=ImageForm_process()
        if form.is_valid():
            form.save()
            img_obj = form.instance
            form_process=ImageForm_process(request.POST)
            imj_obj_process=np.array(img_obj)
            breakpoint()
            myfile = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            img = get_image_intensity(imj_obj_process,int(form_process['min_inten'].value()),int(form_process['max_inten'].value()))
            #img=Image.fromarray(img)
            #if form_process.is_valid():
            #return render(request, 'Protein_interaction.html', {'form': form, 'img_obj': img_obj,'form_process':form_process,'img':img})
            return render(request, 'Protein_interaction.html', {'form': form, 'img_obj': img_obj,'form_process':form_process})

    else:
        form = ImageForm()
        form_process=ImageForm_process()
    return render(request, 'Protein_interaction.html', {'form': form, 'form_process':form_process})

# def test(request):
#     breakpoint()
#     # if request.method == 'POST':
#     #     form_process = ImageForm_process(request.POST)    
#     #     breakpoint()
#     #     if form_process.is_valid():
            
#     #         #pixels=ImageForm.
#     # else:
#     form_process=ImageForm_process()
#     return render(request, 'Protein_interaction.html', {'form_process': form_process})         
    


def image_process(request,img_obj):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm_process(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'index.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'index.html', {'form': form})


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