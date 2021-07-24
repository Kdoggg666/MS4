from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_animals, name='animals'),
    path('care/', views.all_animals_care, name='all_animals_care'),
    path('care/<int:animal_id>/', views.animal_care, name='animal_care'),
    path('<int:animal_id>/', views.animal_details, name='animal_details'),
    path('add/', views.add_animal, name='add_animal'),
    path('edit/<int:animal_id>/', views.edit_animal, name='edit_animal'),
    path('delete/<int:animal_id>/', views.delete_animal,
         name='delete_animal'),
]
