from django.contrib import admin
from django.urls import path
from . import views  #  from the main app dir import the views
from animals.views import all_animals

urlpatterns = [
    path('', views.index, name='home'),  # the index function from views file
    path('', views.all_animals, name='animals'),
]
