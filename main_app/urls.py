from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('animals/', views.animals_index, name='index'),
  path('animals/<int:animal_id>/', views.animals_detail, name='detail'),
]

