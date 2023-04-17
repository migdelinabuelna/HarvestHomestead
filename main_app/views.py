from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from .forms import RegisterForm
from .models import Animal


# Main app 
def home(request):
  return render(request,'home.html')

def about(request):
  return render(request, 'about.html')


##animal resource 

def animals_index(request):
  animal = Animal.objects.all()
  return render(request, 'animals/index.html', {'animal': animal}) #rendeing to folder animas file about
  

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














##feed resource 







#equipment resource 



