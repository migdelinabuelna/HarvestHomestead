from django.forms import ModelForm
from django import forms
from .models import Comment, Farm

class RegisterFarmForm(ModelForm):
    farm_name = forms.CharField(label = 'Farm Name')
    address = forms.CharField(label = 'Farm Address')

    class Meta:
        model = Farm
        fields = ('farm_name', 'address')

class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ('comment',)