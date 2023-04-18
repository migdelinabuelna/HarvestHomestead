from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User


class RegisterFarmForm(ModelForm):
    farm_name = forms.CharField(label = 'Farm Name')
    address = forms.CharField(label = 'Farm Address')

    class Meta:
        model = User
        fields = ('farm_name', 'address')
