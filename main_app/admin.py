from django.contrib import admin
from .models import Animal, Farm, Photo, Crop, Equipment

# Register your models here.

admin.site.register(Animal)
admin.site.register(Farm)
admin.site.register(Photo)
admin.site.register(Crop)
admin.site.register(Equipment)