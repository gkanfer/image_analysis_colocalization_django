from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('Protein_interaction.html',views.Protein_interaction,name='Protein_interaction'),
    path('Image_segmentation.html',views.Image_segmentation,name='Image_segmentation'),
    path('SMLM.html',views.SMLM,name='SMLM'),
    path('Deep_learning.html',views.Deep_learning,name='Deep_learning'),
    path('Genomic_screen.html',views.Genomic_screen,name='Genomic_screen'),]
    # path('index.html', views.image_upload_view,name='index'),]
    #path('upload/', views.image_upload_view)]