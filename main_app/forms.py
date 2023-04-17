from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Farm

class RegisterForm(UserCreationForm):
    username = forms.CharField(label = 'User Name')
    farm_name = forms.CharField(label = 'Farm Name')
    address = forms.CharField(label = 'Address')

    class Meta:
        model = User
        fields = ('username', 'farm_name', 'address')

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit = False)
        Farm.save()
        user.farm_name = self.cleaned_data['farm_name']
        user.address = self.cleaned_data['address']
        if commit:
            user.save()
        return user