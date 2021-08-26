from django import forms
from .models import Upload

class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Upload
        #fields = ('title', 'image','action')
        fields = ('image','action')


# class ImageForm(forms.ModelForm):
#     """Form for the image model"""
#     class Meta:
#         model = Upload
#         #fields = ('title', 'image','action')
#         fields = ('image','action')