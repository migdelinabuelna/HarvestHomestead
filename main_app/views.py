from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from .forms import RegisterForm
from .models import Animal, Photo
import uuid
import boto3

S3_BASE_URL = 'https://s3-us-east-2.amazonaws.com/'
BUCKET = 'harvest-homestead'


# Main app 
def home(request):
  return render(request,'home.html')

def about(request):
  return render(request, 'about.html')


##animal resource 

def animals_index(request):
  animal = Animal.objects.all()
  return render(request, 'animals/index.html', {'animal': animal}) #rendeing to folder animals file about
  

def animals_detail(request, animal_id):
  animal = Animal.objects.get(id=animal_id)
  return render(request, 'animals/detail.html', {'animal': animal})


class AnimalCreate(CreateView):
  model = Animal
  fields = ['name', 'breed', 'preferred_living_conditions']
  success_url = '/animals/'

class AnimalUpdate(UpdateView):
  model = Animal
  fields = ['name', 'breed', 'preferred_living_conditions']
  success_url = '/animals/'
  

class AnimalDelete(DeleteView):
  model = Animal
  success_url = '/animals/'

## accounts

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = RegisterForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invaild sign up - try again'
  form = RegisterForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)






#crops/feed resource 

def crops_index(request):
  return render(request,'crops/index.html')





#equipment resource 

def equipment_index(request):
  return render(request, 'equipment/index.html')



#AWS

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