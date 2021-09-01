from django import forms
from django.db import models
from .models import Upload,test_model

class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Upload
        fields = ['image','min_inten','max_inten',]
        
        # def __str__(self):
        #     return super(self.fields['image'])
class ImageForm_2(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = test_model
        fields = ['image_2','min_inten_2','max_inten_2',]

