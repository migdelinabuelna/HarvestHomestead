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
  path('animals/<int:animal_id>/new_comment', views.animals_new_comment, name='animals_new_comment'),

  #accounts
  path('accounts/signup/', views.signup, name='signup'),
  path('accounts/<int:user_id>/new_farm', views.new_farm, name='new_farm'),

  #feed/crops
  path('crops/', views.crops_index, name='crops_index'),
  path('crops/<int:crop_id>/', views.crops_detail, name='crops_detail'),
  path('crops/create', views.CropsCreate.as_view(), name='crops_create'),
  #we  need to implement delete.
  path('crops/<int:pk>/update/', views.CropsUpdate.as_view(), name='crops_update'),
  path('crops/<int:crop_id>/new_comment', views.crops_new_comment, name='crops_new_comment'),

  #equipment/crops
  path('equipment/', views.equipment_index, name='equipment_index'),
  path('equipment/<int:equipment_id>/', views.equipment_detail, name='equipment_detail'),
  path('equipment/create', views.EquipmentCreate.as_view(), name='equipment_create'),
  path('equipment/<int:pk>/update/', views.EquipmentUpdate.as_view(), name='equipment_update'),

  

  #photo
  path('animals/<int:animal_id>/add_photo', views.add_photo, name='add_photo'),
]

