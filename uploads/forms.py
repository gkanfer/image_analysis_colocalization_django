from django import forms
from django.db import models
from .models import Upload

class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Upload
        fields = ['image','min_inten','max_inten',]
        
        # def __str__(self):
        #     return super(self.fields['image'])


