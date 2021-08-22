from django.urls import path,include
from . import views

urlpatterns = [
    # path('index.html',views.index,name='index'),
    # path('list.html',views.list,name='list'),
    path('home.html',views.home,name='home'),]