from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('animals/', views.animals_index, name='animals_index'),
  path('animals/<int:animal_id>/', views.animals_detail, name='animals_detail'),
  path('animals/create', views.AnimalCreate.as_view(), name='animals_create'),
  path('animals/<int:pk>/update/', views.AnimalUpdate.as_view(), name='animals_update'),
  path('animals/<int:pk>/update/', views.AnimalDelete.as_view(), name='animals_delete'),
  path('accounts/signup/', views.signup, name='signup'),

  #feed/crops
  path('crops/', views.crops_index, name='crops_index'),

  #equipment/crops
  path('equipment/', views.equipment_index, name='equipment_index'),

  #photo
  path('animals/<int:animal_id>/add_photo', views.add_photo, name='add_photo')
]

