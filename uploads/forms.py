from django import forms
from django.db import models
from .models import Upload,set_intensity

class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Upload
        fields = ['image',]
        
        # def __str__(self):
        #     return super(self.fields['image'])


class ImageForm_process(forms.ModelForm):
    """Form for the image model"""
    
    class Meta:
        model = set_intensity
        fields = ['min_inten','max_inten',]