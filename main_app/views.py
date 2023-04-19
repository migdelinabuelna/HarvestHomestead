from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Animal, Photo, Equipment, Crop
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterFarmForm, CommentForm
import uuid
import boto3

S3_BASE_URL = 'https://s3-us-east-2.amazonaws.com/'
BUCKET = 'harvest-homestead'


# Main app
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


# animal resource

def animals_index(request):
    animal = Animal.objects.all()
    # rendeing to folder animals file about
    return render(request, 'animals/index.html', {'animal': animal})


def animals_detail(request, animal_id):
    animal = Animal.objects.get(id=animal_id)
    photo = animal.photo_set.all()
    comment = animal.comment_set.all()
    return render(request, 'animals/detail.html', {'animal': animal, 'photo': photo, 'comment': comment})

class AnimalCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'main_app.add_animal'
    model = Animal
    fields = ['name', 'breed', 'preferred_living_conditions']
    success_url = '/animals/'


class AnimalUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'main_app.change_animal'
    model = Animal
    fields = ['name', 'breed', 'preferred_living_conditions']
    success_url = '/animals/'


class AnimalDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'main_app.delete_animal'
    model = Animal
    success_url = '/animals/'

@login_required
def animals_new_comment(request, animal_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        new_form = form.save(commit=False)
        new_form.animal_id = animal_id
        new_form.user_id = request.user.id
        new_form.save()
    return redirect('home')


# accounts
@permission_required('main_app.view_profile')
def user_index(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'user/profile.html', {'user': user})

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invaild sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

@login_required
@permission_required('main_app.add_farm')
def new_farm(request, user_id):
    error_message = ''
    if request.method == 'POST':
        form = RegisterFarmForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user_id = user_id
            new_form = form.save()
            return redirect('user_index', user_id)
        else:
            error_message = 'Invaild Farm - try again'
    form = RegisterFarmForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/farm.html', context)

# crops/feed resource

def crops_index(request):
    crop = Crop.objects.all()
    return render(request, 'crops/index.html', {'crop': crop})

def crops_detail(request, crop_id):
  crop = Crop.objects.get(id=crop_id)
  return render(request, 'crops/detail.html', {'crop': crop})

class CropsCreate(PermissionRequiredMixin, CreateView):
  permission_required = 'main_app.add_crop'
  model = Crop
  fields = ['name', 'water_dependancy', 'growing_season', 'optimal_growing_conditions', 'average_growth_time']
  success_url = '/crops/'

class CropsUpdate(PermissionRequiredMixin, UpdateView):
  permission_required = 'main_app.change_crop'
  model = Crop
  fields = ['name', 'water_dependancy', 'growing_season', 'optimal_growing_conditions', 'average_growth_time']
  success_url = '/crops/'


# equipment resource

def equipment_index(request):
    equipment = Equipment.objects.all()
    return render(request, 'equipment/index.html', {'equipment': equipment})

def equipment_detail(request, equipment_id):
    equipment = Equipment.objects.get(id=equipment_id)
    comment = equipment.comment_set.all()
    return render(request, 'equipment/detail.html', {'equipment': equipment, 'comment': comment})

@login_required
def equipment_new_comment(request, equipment_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        new_form = form.save(commit=False)
        new_form.equipment_id = equipment_id
        new_form.user_id = request.user.id
        new_form.save()
    return redirect('equipment_detail', equipment_id=equipment_id)


class EquipmentCreate(PermissionRequiredMixin, CreateView):
  permission_required = 'main_app.add_equipment'
  model = Equipment
  fields = ['make', 'model', 'hydraulic_rating', 'year', 'color', 'description', 'fuel_type', 'engine_information']
  success_url = '/equipment/'

class EquipmentUpdate(PermissionRequiredMixin, UpdateView):
  permission_required = 'main_app.change_equipment'
  model = Equipment
  fields = ['make', 'model', 'hydraulic_rating', 'year', 'color', 'description', 'fuel_type', 'engine_information']
  success_url = '/equipment/'


# AWS

@permission_required('main_app.add_photo')
def add_photo(request, animal_id):
    photo_file = request.FILES.get('photo_file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = 'harvest-homestead/' + uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f'{S3_BASE_URL}{BUCKET}/{key}'
            Photo.objects.create(url=url, animal_id=animal_id)
        except:
            print('An error occured uploading file to S3.')
    return redirect('animals_detail', animal_id=animal_id)

