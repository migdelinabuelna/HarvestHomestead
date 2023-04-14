from django.shortcuts import render

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
