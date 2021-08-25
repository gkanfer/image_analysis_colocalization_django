from django.shortcuts import render
from .forms import ImageForm
import pdb

def home(request):
    return render(request,'home.html',{})

def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'index.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'index.html', {'form': form})


def Protein_interaction(request):
    return render(request,'Protein_interaction.html',{})

def Image_segmentation(resquset):
    return render(resquset,'Image_segmentation.html',{})

def SMLM(resquset):
    return render(resquset,'SMLM.html',{})

def Deep_learning(resquset):
    return render(resquset,'Deep_learning.html',{})

def Genomic_screen(resquset):
    return render(resquset,'Genomic_screen.html',{})