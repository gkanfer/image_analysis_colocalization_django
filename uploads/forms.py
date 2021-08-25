from django import forms
from .models import Upload

class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Upload
        fields = ('title', 'image')