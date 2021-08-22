from django.shortcuts import render 
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Upload
from .utils import get_image
import pdb


def home(request):
    breakpoint()
    document = Upload.image.get(pk=1)
    return render(request,'index.html',{"document":document})

def process(request):
    pass



def index(request):
    return render(request,'index.html',{})

    # change the text and save for example